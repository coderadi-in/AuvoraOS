// | Virtual file management class
class VirtualFileSystem {
    constructor() {
        this.root = { "A://": {} };
        this.meta = {};
        this.load();
    }

    // & function to parse a filepath
    _traverse(path, createMissing = false) {
        const parts = path.replace("A://", "").split('/').filter(Boolean);
        let current = this.root['A://'];

        for (let i = 0; i < parts.length; i++) {
            const part = parts[i];

            if (!current[part]) {
                if (!createMissing) {
                    throw new Error(`Path not found: ${path}`)
                } else {
                    current[part] = {}
                }
            }

            current = current[part];
        }

        return current;
    }

    // & create new folder
    mkdir(path) {
        this._traverse(path, true);
        this._updateMeta(path);
        this.save();
    }

    // & create new file
    write(path, content) {
        const parts = path.split('/');
        const filename = parts.pop();
        const dirPath = parts.join('/')

        const dir = this._traverse(dirPath, true);
        dir[filename] = content;

        this._updateMeta();
        this.save();
    }

    // & read a file
    read(path) {
        const parts = path.split('/');
        const fileName = parts.pop();
        const dirPath = parts.join('/');

        const dir = this._traverse(dirPath);
        const content = dir[fileName];

        if (content === undefined) throw new Error(`File not found: ${path}`);
        return content;
    }

    // & delete a file
    delete(path) {
        const parts = path.split('/');
        const name = parts.pop();
        const dirPath = parts.join('/');

        const dir = this._traverse(dirPath);
        delete dir[name];
        delete this.meta[path];
        this.save();
    }

    list(path = 'A://') {
        const dir = this._traverse(path);
        return Object.keys(dir);
    }

    // & Add or update metadata
    _updateMeta(path, type, content = null) {
        this.meta[path] = {
            type,
            size: type === 'file' ? content.length : 0,
            createdAt: new Date().toISOString(),
            modifiedAt: new Date().toISOString(),
        };
    }

    // & Save to localStorage
    async save() {
        await fetch('/api/save', {
            method: 'POST',
            body: {
                root: this.root,
                meta: this.meta,
            }
        })
    }

    // & Load from server
    async load() {
        const data = await fetch('/api/load');
        if (data) {
            const parsed = await data.json();
            this.root = parsed.root;
            this.meta = parsed.meta;
            console.log(this.root, this.meta);            
        }
    }

    // & Reset filesystem (careful!)
    format() {
        this.root = { 'A://': {} };
        this.meta = {};
        this.save();
        console.log('File system formatted.');
    }

}

// | Export the VFS system
export const vfs = new VirtualFileSystem();