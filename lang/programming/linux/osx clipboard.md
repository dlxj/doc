cat myfile.txt | pbcopy



## pbcopy

This command allows you to copy text from stdin into the clipboard[1](https://langui.sh/2010/11/14/pbpaste-pbcopy-in-mac-os-x-or-terminal-clipboard-fun/#fn:1) buffer. Trivial example:

```bash
echo 'Hello World!' | pbcopy 
```

"Hello World!" is now in your clipboard.

## pbpaste

Pastes from your clipboard to stdout. Trivial example:

```bash
echo `pbpaste` 
```

This will echo the contents of your clipboard. If you're following along you'll see "Hello World!".

