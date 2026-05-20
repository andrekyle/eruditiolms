class RichTextEditor {
    constructor(targetElement, options = {}) {
        this.target = targetElement;
        this.options = {
            height: options.height || '200px',
            placeholder: options.placeholder || 'Start typing...',
            toolbar: options.toolbar || [
                'bold', 'italic', 'underline', 'strikethrough',
                'heading1', 'heading2',
                'bulletList', 'numberedList',
                'link', 'image',
                'alignLeft', 'alignCenter', 'alignRight',
                'undo', 'redo'
            ]
        };
        this.init();
    }

    init() {
        // Create editor container
        this.container = document.createElement('div');
        this.container.className = 'rich-editor-container';
        this.target.parentNode.insertBefore(this.container, this.target);
        this.target.style.display = 'none';

        // Create toolbar
        this.toolbar = document.createElement('div');
        this.toolbar.className = 'rich-editor-toolbar';
        this.container.appendChild(this.toolbar);

        // Create editor content area
        this.editor = document.createElement('div');
        this.editor.className = 'rich-editor-content';
        this.editor.contentEditable = true;
        this.editor.style.height = this.options.height;
        this.editor.dataset.placeholder = this.options.placeholder;
        this.container.appendChild(this.editor);

        this.setupToolbar();
        this.setupEventListeners();
        this.syncContent();
    }

    setupToolbar() {
        // Inline SVG icons (Boxicons paths) so the toolbar renders even if the
        // icon font CDN fails to load.
        const SVG = (path) => `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">${path}</svg>`;
        const icons = {
            bold:          SVG('<path d="M15.6 11.4A4 4 0 0 0 13 4H7v16h7a4.5 4.5 0 0 0 1.6-8.6zM10 6.5h2.5a1.5 1.5 0 0 1 0 3H10v-3zm3.5 11H10v-3.5h3.5a1.75 1.75 0 0 1 0 3.5z"/>'),
            italic:        SVG('<path d="M10 4v3h2.21l-3.42 8H6v3h8v-3h-2.21l3.42-8H18V4z"/>'),
            underline:     SVG('<path d="M6 3v9a6 6 0 0 0 12 0V3h-2v9a4 4 0 0 1-8 0V3H6zm-1 17h14v2H5z"/>'),
            strikethrough: SVG('<path d="M3 11h18v2H3zM8 7a4 4 0 0 1 4-3 4 4 0 0 1 4 3h-2a2 2 0 0 0-4 0H8zm0 6h8a4 4 0 0 1-4 5 4 4 0 0 1-4-5z"/>'),
            heading1:      SVG('<path d="M4 4h2v7h6V4h2v16h-2v-7H6v7H4V4zm14 4h3v12h-2v-9.5l-2 .5V9l1-1z"/>'),
            heading2:      SVG('<path d="M4 4h2v7h6V4h2v16h-2v-7H6v7H4V4zm14 16v-1.5l3.4-3.1c.7-.7 1.1-1.3 1.1-2.1 0-1-.7-1.5-1.7-1.5-1 0-1.7.6-1.7 1.6h-2c0-2.1 1.6-3.4 3.8-3.4 2.1 0 3.6 1.1 3.6 3 0 1.3-.8 2.3-1.9 3.3L18.8 18H23v2h-5z"/>'),
            bulletList:    SVG('<path d="M4 6h2v2H4zm0 5h2v2H4zm0 5h2v2H4zm4-10h12v2H8zm0 5h12v2H8zm0 5h12v2H8z"/>'),
            numberedList:  SVG('<path d="M3 4h2v4H4V5H3V4zm0 7h2.5L3 13.5V15h4v-1H4.5L7 11.5V10H3v1zm0 5h2v.5H4v1h1v.5H3v1h4v-4H3v1zm6-12h12v2H9zm0 5h12v2H9zm0 5h12v2H9z"/>'),
            link:          SVG('<path d="M10.59 13.41a1 1 0 0 0 1.41 0l4-4a3 3 0 0 0-4.24-4.24l-1.42 1.42 1.42 1.41 1.41-1.41a1 1 0 0 1 1.41 1.41l-4 4a1 1 0 0 0 0 1.41zm2.82-2.82a1 1 0 0 0-1.41 0l-4 4a3 3 0 0 0 4.24 4.24l1.42-1.42-1.42-1.41-1.41 1.41a1 1 0 0 1-1.41-1.41l4-4a1 1 0 0 0 0-1.41z"/>'),
            image:         SVG('<path d="M19 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2zm0 16H5V5h14v14zm-9-7l-3 4h10l-4-5-3 3-1-1z"/>'),
            alignLeft:     SVG('<path d="M3 4h18v2H3zm0 5h12v2H3zm0 5h18v2H3zm0 5h12v2H3z"/>'),
            alignCenter:   SVG('<path d="M3 4h18v2H3zm3 5h12v2H6zm-3 5h18v2H3zm3 5h12v2H6z"/>'),
            alignRight:    SVG('<path d="M3 4h18v2H3zm6 5h12v2H9zm-6 5h18v2H3zm6 5h12v2H9z"/>'),
            undo:          SVG('<path d="M12 5V2L7 6l5 4V7a6 6 0 0 1 0 12 6 6 0 0 1-6-6H4a8 8 0 1 0 8-8z"/>'),
            redo:          SVG('<path d="M12 5V2l5 4-5 4V7a6 6 0 0 0 0 12 6 6 0 0 0 6-6h2a8 8 0 1 1-8-8z"/>'),
        };
        const toolbarItems = {
            bold:          { icon: icons.bold,          command: 'bold' },
            italic:        { icon: icons.italic,        command: 'italic' },
            underline:     { icon: icons.underline,     command: 'underline' },
            strikethrough: { icon: icons.strikethrough, command: 'strikethrough' },
            heading1:      { icon: icons.heading1,      command: 'formatBlock', value: 'h1' },
            heading2:      { icon: icons.heading2,      command: 'formatBlock', value: 'h2' },
            bulletList:    { icon: icons.bulletList,    command: 'insertUnorderedList' },
            numberedList:  { icon: icons.numberedList,  command: 'insertOrderedList' },
            link:          { icon: icons.link,          command: 'createLink' },
            image:         { icon: icons.image,         command: 'insertImage' },
            alignLeft:     { icon: icons.alignLeft,     command: 'justifyLeft' },
            alignCenter:   { icon: icons.alignCenter,   command: 'justifyCenter' },
            alignRight:    { icon: icons.alignRight,    command: 'justifyRight' },
            undo:          { icon: icons.undo,          command: 'undo' },
            redo:          { icon: icons.redo,          command: 'redo' },
        };

        this.options.toolbar.forEach(item => {
            const toolbarItem = toolbarItems[item];
            if (toolbarItem) {
                const button = document.createElement('button');
                button.type = 'button';
                button.className = 'rich-editor-button';
                button.innerHTML = toolbarItem.icon;
                button.title = item.charAt(0).toUpperCase() + item.slice(1);

                button.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.execCommand(toolbarItem.command, toolbarItem.value);
                });

                this.toolbar.appendChild(button);
            }
        });
    }

    setupEventListeners() {
        this.editor.addEventListener('input', () => this.syncContent());
        this.editor.addEventListener('keydown', (e) => {
            if (e.key === 'Tab') {
                e.preventDefault();
                document.execCommand('insertHTML', false, '&#009');
            }
        });

        // Handle paste to strip formatting
        this.editor.addEventListener('paste', (e) => {
            e.preventDefault();
            const text = e.clipboardData.getData('text/plain');
            document.execCommand('insertText', false, text);
        });
    }

    execCommand(command, value = null) {
        this.editor.focus();
        if (command === 'createLink') {
            const url = prompt('Enter URL:');
            if (url) {
                document.execCommand(command, false, url);
            }
        } else if (command === 'insertImage') {
            const url = prompt('Enter image URL:');
            if (url) {
                document.execCommand(command, false, url);
            }
        } else {
            document.execCommand(command, false, value);
        }
        this.syncContent();
    }

    syncContent() {
        this.target.value = this.editor.innerHTML;
        this.target.dispatchEvent(new Event('change'));
    }

    getContent() {
        return this.editor.innerHTML;
    }

    setContent(html) {
        this.editor.innerHTML = html;
        this.syncContent();
    }
}
