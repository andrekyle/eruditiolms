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
        const toolbarItems = {
            bold: { icon: 'bx-bold', command: 'bold', type: 'button' },
            italic: { icon: 'bx-italic', command: 'italic', type: 'button' },
            underline: { icon: 'bx-underline', command: 'underline', type: 'button' },
            strikethrough: { icon: 'bx-strikethrough', command: 'strikethrough', type: 'button' },
            heading1: { icon: 'bx-heading', command: 'formatBlock', value: 'h1', type: 'button' },
            heading2: { icon: 'bx-heading', command: 'formatBlock', value: 'h2', type: 'button' },
            bulletList: { icon: 'bx-list-ul', command: 'insertUnorderedList', type: 'button' },
            numberedList: { icon: 'bx-list-ol', command: 'insertOrderedList', type: 'button' },
            link: { icon: 'bx-link', command: 'createLink', type: 'button' },
            image: { icon: 'bx-image', command: 'insertImage', type: 'button' },
            alignLeft: { icon: 'bx-align-left', command: 'justifyLeft', type: 'button' },
            alignCenter: { icon: 'bx-align-middle', command: 'justifyCenter', type: 'button' },
            alignRight: { icon: 'bx-align-right', command: 'justifyRight', type: 'button' },
            undo: { icon: 'bx-undo', command: 'undo', type: 'button' },
            redo: { icon: 'bx-redo', command: 'redo', type: 'button' }
        };

        this.options.toolbar.forEach(item => {
            const toolbarItem = toolbarItems[item];
            if (toolbarItem) {
                const button = document.createElement('button');
                button.type = 'button';
                button.className = 'rich-editor-button';
                button.innerHTML = `<i class="bx ${toolbarItem.icon}"></i>`;
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
