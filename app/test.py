/* Code comment style */
.mtk3 {
    font-family: 'Monaspace Radon', monospace !important;
    color: #008c7d !important;
}

.line-numbers {
    position: relative !important;
    width: 35px !important;
    font-size: 16px !important;
    font-family: 'Geist Mono' !important;
    opacity: .3;
}

/* Code canvas top shadow */
.monaco-editor .scroll-decoration {
    box-shadow: 0px 0px 20px rgba(0, 0, 0, .75) !important;
    top: -6px !important;
}

/* Toolbars when tabs are enabled. */
.monaco-workbench .part.editor>.content .editor-group-container>.title .editor-actions {
    display: none !important;
}

/* Side bar */
.part.sidebar {
    box-shadow: 0px 0px 50px rgba(0, 0, 0, .25);
}

/* File Explorer Selected Item */
.monaco-list.list_id_1 .monaco-list-row.selected {
    background-color: #4f5971 !important;
    opacity: 1 !important;
    border-top: 1px #727b90 solid;
    border-bottom: 1px #727b90 solid;
}

/* List item label name */
.monaco-list.list_id_1 .monaco-list-row.selected .label-name {
    color: #fff !important;
    opacity: 1 !important;
}

/* File explorer action buttons */
.monaco-workbench .part.sidebar .title-actions .actions-container {
    display: none;
}

/* File Explorer Item Label */
.monaco-tree .monaco-tree-row .label-name,
.monaco-list .monaco-list-row
.monaco-icon-label .label-name {
    font-family: 'Geist Mono', monospace !important;
    font-size: 14px !important;
    font-weight: 400 !important;
    color: #FFF !important;
}

/* Sidebar top shadow */
.monaco-scrollable-element>.shadow.top {
    box-shadow: 0px 0px 10px rgba(0,0,0,.75) !important;
    top: -3px !important;
}

/* Sidebar title */
.composite.title {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-items: center !important;
}
.composite.title h2 {
    font-weight: bold !important;
    font-size: 12px !important;
    text-transform: uppercase;
    color: #bc9abc !important;
}

.composite.title h2::before {
    display: inline-block;
    margin-right: 6px;
    font-size: 1.1rem;
    content: '🚀';
}

/* Scroll Bar */
.slider {
    position: absolute !important;
    right: 1px !important;
    width: 1px !important;
    background: #bc9abc !important;
    left: auto !important;
}

.codicon-toolbar-more, .codicon-word-wrap {
    display: block !important;
}

/* Tooltip box style */
.monaco-editor-hover,
.monaco-hover {
    box-shadow: 0px 8px 32px rgba(0,0,0,.45) !important;
    padding: 10px !important;
    background-image: linear-gradient(#3c3c50 0%, #2a2b38 100%) !important;
    backdrop-filter: blur(3px) !important;
    border-radius: 20px !important;
    border: none !important
}

/* Project title's style at the top. */
.monaco-workbench .part.titlebar>.titlebar-container>.titlebar-center>.window-title>.command-center .action-item.command-center-center {
    border: none !important;
    background: transparent !important;
}

/* Project Title */
.titlebar-left {
    justify-content: flex-start !important;
    flex-grow: 0 !important;
    width: auto !important;
}

/* Search Label */
.search-label {
    font-family: 'Geist Mono' !important;
    font-size: 14px !important;
    color: #fff;
    display: block;
}

/* Search icon */
.search-icon {
    display: none !important;
}

.codicon-search::before {
    display: none !important;
}

.codicon-arrow-right, .codicon-arrow-left {
    display: none !important;
}

.titlebar-right > * {
    display: none !important;
}

/* Command Palette */
.quick-input-widget {
    transform: translateY(-50%) !important;
    top: 50% !important;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, .45) !important;
    padding: 10px 10px 18px 10px !important;
    background-image: linear-gradient(#3c3c50 0%, #2a2b38 100%) !important;
    backdrop-filter: blur(3px) !important;
    border-radius: 20px !important;
}

/* Remove background for lists */
.monaco-list-rows {
    background: transparent !important;
}

/* List hover */
.monaco-list-row:hover {
    background: rgba(0, 0, 0, .2) !important;
}

.notifications-toasts .monaco-list-row:hover {
    background: none !important;
}

/* .monaco-list-row.focused {
    background-color: rgb(181 198 228 / 25%) !important;
} */

/* .synthetic-focus {
    outline-color: rgba(50, 50, 50, 1) !important;
} */

/* .quick-input-widget .monaco-label {
    font-size: 11px !important;
} */

/* Command palette text input */
.quick-input-filter .monaco-inputbox {
    border-radius: 12px !important;
    padding: 8px !important;
    border: none !important;
    background-color: rgba(34, 34, 34, .40) !important;
    font-family: "Geist Mono" !important;
    font-size: 14px !important;
    margin-bottom: 16px !important;
}

#command-blur {
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, .15);
    top: 0;
    left: 0;
    backdrop-filter: blur(8px);
}

/* Command palette's input box placeholder. */
.monaco-inputbox input::placeholder {
    color: rgba(255, 255, 255, .3) !important;
}

/* .monaco-workbench label {
    color: #fff !important;
    font-size: 14px !important;
} */

/* Container that holds the VS Code home icon. */
.editor-group-watermark {
    max-width: none !important;
}

.command-center-center {
    width:  auto !important;
}

