/* dark-select.js
 * Progressively replaces every native <select> (single-value only) with a
 * fully-styleable custom dropdown so the popup list matches the dark theme.
 * The original <select> stays in the DOM (visually hidden) so forms still work.
 */
(function () {
    'use strict';

    function enhance(select) {
        if (select.dataset.dsEnhanced === '1') return;
        if (select.multiple) return;
        if (select.size && select.size > 1) return;
        if (select.disabled) { /* still enhance, but mark */ }

        select.dataset.dsEnhanced = '1';

        // Wrapper
        var wrap = document.createElement('div');
        wrap.className = 'ds-select';
        if (select.disabled) wrap.classList.add('is-disabled');

        // Trigger button
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'ds-select__btn';
        btn.setAttribute('aria-haspopup', 'listbox');
        btn.setAttribute('aria-expanded', 'false');
        if (select.disabled) btn.disabled = true;

        var label = document.createElement('span');
        label.className = 'ds-select__label';
        var caret = document.createElement('span');
        caret.className = 'ds-select__caret';
        caret.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>';
        btn.appendChild(label);
        btn.appendChild(caret);

        // Popup list
        var list = document.createElement('ul');
        list.className = 'ds-select__list';
        list.setAttribute('role', 'listbox');
        list.hidden = true;

        function rebuildOptions() {
            list.innerHTML = '';
            Array.prototype.forEach.call(select.options, function (opt, idx) {
                var li = document.createElement('li');
                li.className = 'ds-select__opt';
                li.setAttribute('role', 'option');
                li.dataset.value = opt.value;
                li.dataset.index = String(idx);
                li.textContent = opt.text;
                if (opt.disabled) li.classList.add('is-disabled');
                if (opt.selected) {
                    li.classList.add('is-selected');
                    li.setAttribute('aria-selected', 'true');
                }
                li.addEventListener('mousedown', function (e) { e.preventDefault(); });
                li.addEventListener('click', function () {
                    if (opt.disabled) return;
                    select.selectedIndex = idx;
                    syncLabel();
                    select.dispatchEvent(new Event('input', { bubbles: true }));
                    select.dispatchEvent(new Event('change', { bubbles: true }));
                    close();
                    btn.focus();
                });
                list.appendChild(li);
            });
        }

        function syncLabel() {
            var sel = select.options[select.selectedIndex];
            label.textContent = sel ? sel.text : '';
            Array.prototype.forEach.call(list.children, function (li) {
                var isSel = Number(li.dataset.index) === select.selectedIndex;
                li.classList.toggle('is-selected', isSel);
                if (isSel) li.setAttribute('aria-selected', 'true');
                else li.removeAttribute('aria-selected');
            });
        }

        function open() {
            if (select.disabled) return;
            rebuildOptions();
            list.hidden = false;
            btn.setAttribute('aria-expanded', 'true');
            wrap.classList.add('is-open');
            document.addEventListener('mousedown', onDocClick, true);
            document.addEventListener('keydown', onKey, true);
            // Scroll selected into view
            var sel = list.querySelector('.is-selected');
            if (sel) sel.scrollIntoView({ block: 'nearest' });
        }
        function close() {
            list.hidden = true;
            btn.setAttribute('aria-expanded', 'false');
            wrap.classList.remove('is-open');
            document.removeEventListener('mousedown', onDocClick, true);
            document.removeEventListener('keydown', onKey, true);
        }
        function onDocClick(e) { if (!wrap.contains(e.target)) close(); }
        function onKey(e) {
            if (e.key === 'Escape') { e.preventDefault(); close(); btn.focus(); return; }
            if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
                e.preventDefault();
                var dir = e.key === 'ArrowDown' ? 1 : -1;
                var n = select.options.length;
                var i = select.selectedIndex;
                for (var step = 0; step < n; step++) {
                    i = (i + dir + n) % n;
                    if (!select.options[i].disabled) { select.selectedIndex = i; break; }
                }
                syncLabel();
                select.dispatchEvent(new Event('input', { bubbles: true }));
                select.dispatchEvent(new Event('change', { bubbles: true }));
            }
            if (e.key === 'Enter') { e.preventDefault(); close(); btn.focus(); }
        }

        btn.addEventListener('click', function () {
            if (list.hidden) open(); else close();
        });
        btn.addEventListener('keydown', function (e) {
            if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
                e.preventDefault(); open();
            }
        });

        // Mount: insert wrap before the select, move select inside (hidden), then list
        select.parentNode.insertBefore(wrap, select);
        wrap.appendChild(select);
        wrap.appendChild(btn);
        wrap.appendChild(list);
        select.classList.add('ds-select__native');

        // Copy width-affecting classes (uui-filter-select, form-select) onto wrapper for sizing hooks
        if (select.classList.contains('uui-filter-select')) wrap.classList.add('ds-select--uui');
        if (select.classList.contains('form-select')) wrap.classList.add('ds-select--form');
        if (select.classList.contains('form-select-sm')) wrap.classList.add('ds-select--sm');
        if (select.classList.contains('form-select-lg')) wrap.classList.add('ds-select--lg');

        rebuildOptions();
        syncLabel();

        // Keep label in sync if the underlying select changes programmatically
        select.addEventListener('change', syncLabel);
    }

    function enhanceAll(root) {
        var nodes = (root || document).querySelectorAll('select');
        Array.prototype.forEach.call(nodes, enhance);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () { enhanceAll(); });
    } else {
        enhanceAll();
    }

    // Expose for dynamically-added selects
    window.DarkSelect = { enhance: enhance, enhanceAll: enhanceAll };
})();
