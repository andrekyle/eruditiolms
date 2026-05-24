/* Icons shim — converts legacy Boxicons (<i class="bx bx-NAME">) to
 * thin-line Lucide SVG icons (Microsoft Fluent / Azure aesthetic).
 * Loaded after lucide.min.js. */
(function () {
    "use strict";

    // Boxicons class -> Lucide icon name (kebab-case).
    var MAP = {
        "bx-home": "home",
        "bx-code-alt": "code",
        "bx-code-block": "code-2",
        "bx-test-tube": "flask-conical",
        "bx-dashboard": "layout-dashboard",
        "bx-book": "book",
        "bx-book-open": "book-open",
        "bx-book-content": "book-open-text",
        "bx-task": "list-checks",
        "bx-cog": "settings",
        "bx-show": "eye",
        "bx-error": "alert-circle",
        "bx-calendar": "calendar",
        "bx-menu": "menu",
        "bx-edit": "pencil",
        "bx-key": "key",
        "bx-trash": "trash-2",
        "bx-save": "save",
        "bx-lock-alt": "lock",
        "bx-envelope": "mail",
        "bx-chalkboard": "presentation",
        "bx-check": "check",
        "bx-check-circle": "check-circle",
        "bx-info-circle": "info",
        "bx-help-circle": "help-circle",
        "bx-plus": "plus",
        "bx-plus-circle": "plus-circle",
        "bx-play": "play",
        "bx-reset": "rotate-ccw",
        "bx-trophy": "trophy",
        "bx-arrow-back": "arrow-left",
        "bx-right-arrow-alt": "arrow-right",
        "bx-chevron-left": "chevron-left",
        "bx-chevron-right": "chevron-right",
        "bx-chevron-up": "chevron-up",
        "bx-chevron-down": "chevron-down",
        "bx-log-in": "log-in",
        "bx-log-in-circle": "log-in",
        "bx-log-out": "log-out",
        "bx-user": "user",
        "bx-user-circle": "user-circle",
        "bx-user-plus": "user-plus",
        "bx-user-check": "user-check",
        "bx-user-minus": "user-minus",
        "bx-user-x": "user-x",
        "bx-user-voice": "users",
        "bx-medal": "trophy",
        "bx-list-ol": "list-ordered",
        "bx-list-check": "list-checks",
        "bx-list-ul": "list",
        "bx-play-circle": "play-circle",
        "bx-edit-alt": "pencil-line",
        "bx-pencil": "pencil",
        "bx-pencil-square": "square-pen",
        "bx-receipt": "file-text",
        "bx-file": "file-text",
        "bx-id-card": "id-card",
        "bx-clipboard": "clipboard",
        "bx-time": "clock",
        "bx-line-chart": "line-chart",
        "bx-bar-chart": "bar-chart-3",
        "bx-bar-chart-alt": "bar-chart-3",
        "bx-bar-chart-alt-2": "bar-chart-3",
        "bx-bar-chart-square": "bar-chart-3",
        "bx-stats": "activity",
        "bx-trending-up": "trending-up"
    };

    var FALLBACK = "circle";

    function convert() {
        if (typeof lucide === "undefined") return;
        var nodes = document.querySelectorAll("i.bx");
        nodes.forEach(function (el) {
            var name = null;
            for (var i = 0; i < el.classList.length; i++) {
                var c = el.classList[i];
                if (c.indexOf("bx-") === 0 && MAP[c]) {
                    name = MAP[c];
                    break;
                }
            }
            if (!name) name = FALLBACK;
            el.setAttribute("data-lucide", name);
            // Remove bx classes so boxicons font stops affecting layout.
            for (var j = el.classList.length - 1; j >= 0; j--) {
                var cls = el.classList[j];
                if (cls === "bx" || cls.indexOf("bx-") === 0) {
                    el.classList.remove(cls);
                }
            }
            el.classList.add("icon");
        });
        try {
            lucide.createIcons({
                attrs: {
                    "stroke-width": 1.25,
                    "width": "1em",
                    "height": "1em"
                }
            });
        } catch (e) {
            // no-op
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", convert);
    } else {
        convert();
    }

    // Expose for dynamic content.
    window.refreshIcons = convert;
})();
