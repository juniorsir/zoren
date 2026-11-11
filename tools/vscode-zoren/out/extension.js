"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;

const path = require("path");
const fs = require("fs");
const vscode = require("vscode");
let node_1;
try {
    node_1 = require("vscode-languageclient/node");
} catch (e) {
    node_1 = null;
}

let client;
let terminal;

function findCompilerPath() {
    const config = vscode.workspace.getConfiguration('zoren');
    let compilerPath = config.get('compilerPath');
    if (compilerPath && fs.existsSync(compilerPath)) {
        return compilerPath;
    }

    if (vscode.workspace.workspaceFolders && vscode.workspace.workspaceFolders.length > 0) {
        const root = vscode.workspace.workspaceFolders[0].uri.fsPath;
        const candidateWorkspace = path.join(root, 'bin', 'zoren');
        if (fs.existsSync(candidateWorkspace)) {
            return candidateWorkspace;
        }
    }

    const systemPaths = [
        '/usr/local/bin/zoren',
        path.join(process.env.HOME || '/root', '.zoren', 'bin', 'zoren'),
        '/usr/bin/zoren'
    ];

    for (const p of systemPaths) {
        if (fs.existsSync(p)) {
            return p;
        }
    }

    return 'zoren';
}

function getOrCreateTerminal() {
    if (!terminal || terminal.exitStatus !== undefined) {
        terminal = vscode.window.createTerminal({ name: 'Zoren Studio' });
    }
    return terminal;
}

function activate(context) {
    const compiler = findCompilerPath();

    // 1. Language Server Protocol integration
    if (node_1) {
        try {
            const serverOptions = {
                command: compiler,
                args: ['lsp'],
                options: { env: process.env }
            };

            const clientOptions = {
                documentSelector: [{ scheme: 'file', language: 'zoren' }],
                synchronize: {
                    fileEvents: vscode.workspace.createFileSystemWatcher('**/*.zor')
                }
            };

            client = new node_1.LanguageClient('zorenLanguageServer', 'Zoren Language Server', serverOptions, clientOptions);
            client.start();
            console.log('Zoren LSP Extension activated with compiler:', compiler);
        } catch (err) {
            console.warn('Zoren LSP failed to initialize:', err);
        }
    }

    // 2. Command: Run active file
    const runCmd = vscode.commands.registerCommand('zoren.run', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage('No active Zoren file open to run.');
            return;
        }
        const filePath = editor.document.fileName;
        const term = getOrCreateTerminal();
        term.show();
        term.sendText(`${compiler} run "${filePath}"`);
    });

    // 3. Command: Build active file
    const buildCmd = vscode.commands.registerCommand('zoren.build', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage('No active Zoren file open to compile.');
            return;
        }
        const filePath = editor.document.fileName;
        const term = getOrCreateTerminal();
        term.show();
        term.sendText(`${compiler} "${filePath}"`);
    });

    // 4. Command: Check / Doctor active file
    const checkCmd = vscode.commands.registerCommand('zoren.check', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage('No active Zoren file open to check.');
            return;
        }
        const filePath = editor.document.fileName;
        const term = getOrCreateTerminal();
        term.show();
        term.sendText(`${compiler} doctor "${filePath}"`);
    });

    // 5. Command: Format document
    const formatCmd = vscode.commands.registerCommand('zoren.format', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;
        const filePath = editor.document.fileName;
        const term = getOrCreateTerminal();
        term.show();
        term.sendText(`${compiler} fmt "${filePath}"`);
    });

    // 6. Command: Open Interactive REPL Studio
    const replCmd = vscode.commands.registerCommand('zoren.repl', () => {
        const term = getOrCreateTerminal();
        term.show();
        term.sendText(`${compiler} repl`);
    });

    // 7. Status Bar Item
    const statusBar = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Right, 100);
    statusBar.text = '$(zap) Zoren';
    statusBar.tooltip = 'Zoren Toolchain & Studio (Click for Actions)';
    statusBar.command = 'zoren.menu';
    statusBar.show();

    const menuCmd = vscode.commands.registerCommand('zoren.menu', async () => {
        const choice = await vscode.window.showQuickPick([
            { label: '$(play) Run Current File', command: 'zoren.run' },
            { label: '$(package) Compile Current File', command: 'zoren.build' },
            { label: '$(pulse) Run Doctor Diagnostics', command: 'zoren.check' },
            { label: '$(check) Format Document', command: 'zoren.format' },
            { label: '$(terminal) Launch REPL Studio', command: 'zoren.repl' }
        ], { placeHolder: 'Select Zoren action to execute' });

        if (choice) {
            vscode.commands.executeCommand(choice.command);
        }
    });

    context.subscriptions.push(runCmd, buildCmd, checkCmd, formatCmd, replCmd, menuCmd, statusBar);
}

function deactivate() {
    if (!client) {
        return undefined;
    }
    return client.stop();
}
