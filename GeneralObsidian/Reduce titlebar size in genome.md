


16

[](https://askubuntu.com/posts/1358674/timeline)

Surprisingly, this common question apparently was never posted here before - I searched a duplicate in vain.

Gnome does not expose detailed tweaking of the appearance to the users. It does not even expose changing a theme - you need to install Gnome Tweaks for that.

The easiest option to change the height of a title bar is to change to a appropriate theme. This, however, is an all-or-nothing approach. You have to take the entire theme as is.

You probably better of with [some manual coding](https://unix.stackexchange.com/questions/276951/how-to-change-the-titlebar-height-in-standard-gtk-apps-and-those-with-headerbars?noredirect=1&lq=1). Create a file `~/.config/gtk-3.0/gtk.css` and enter or adapt the following css code:

```
headerbar entry,
headerbar spinbutton,
headerbar button,
headerbar separator {
    margin-top: 0px; /* same as headerbar side padding for nicer proportions */
    margin-bottom: 0px;
}

headerbar {
    min-height: 24px;
    padding-left: 2px; /* same as childrens vertical margins for nicer proportions */
    padding-right: 2px;
    margin: 0px; /* same as headerbar side padding for nicer proportions */
    padding: 0px;
}
```

Log out and then back in for the changes to take effect (or reset Gnome Shell with Alt+F2, r when on Xorg).












-----------------------------------------------



The short answer is that you can tweak the button “container” (its padding, margins, and minimum size) via your gtk.css file—but the actual icon size isn’t freely scalable via CSS. In GTK+3 the headerbar (or client‐side decoration) buttons (minimize, maximize/close, “new terminal”, etc.) display images that come from your icon theme at a predetermined size (often using “symbolic” icons). This design is intentional to ensure icons remain crisp and consistent; they’re rendered from pre‐sized assets.

You have two options:

1. **Adjust the Button “Chrome”:**  
       You can make the buttons appear smaller by reducing the padding, margins, and minimum dimensions. For example, you might add something like the following to your `~/.config/gtk-3.0/gtk.css` file:

```css
/* Reduce the headerbar button area */
headerbar .titlebutton {
    padding: 2px;
    margin: 0;
    min-width: 16px;
    min-height: 16px;
}
```

This code shrinks the button’s “chrome” (the space around the icon), which may give the impression of smaller controls. (Note that the actual icon image may still be drawn at its theme-defined size.)

2. **Change the Icon Assets:**  
       Because the icons themselves are chosen from the icon theme (for example, the “window-close-symbolic” icon), you cannot force GTK+3 to render them at an arbitrary size via CSS. Some have tried applying a transform with code like:

```css
headerbar .titlebutton image {
    -gtk-icon-transform: scale(0.8);
}
```

—but support for such a property isn’t officially documented and may not work reliably across versions. In practice, if you want genuinely smaller headerbar icons, the most robust approach is to switch to an icon theme that provides smaller versions of those icons (or modify the icon theme yourself).

### In Summary

- **CSS adjustments:** You can reduce the surrounding padding and minimum sizes (as in the first code block), which may help the overall look.
- **Icon theme limitation:** The intrinsic size of the headerbar icons is controlled by the icon theme (and by GTK’s handling of symbolic icons), so CSS cannot simply “shrink” them.

This behavior has been noted by other users; for instance, in discussions about headerbar icon sizes in GNOME it’s often mentioned that “you can’t resize icons” because the icon theme defines them (see discussions on r/gnome and related Stack Overflow threads , ).

If your goal is to have a more compact terminal window appearance, try first adjusting the padding/margin settings in gtk.css. If that isn’t enough, consider either choosing a different icon theme or editing the theme’s icon assets to provide smaller images.

Remember to log out/in or restart the GNOME Shell (using Alt+F2, then type “r” on Xorg) for changes to take effect.



---------------------------------------------------------------


The search and "new terminal" buttons are part of the GNOME Terminal's headerbar and are likely controlled separately from the window control buttons (minimize, maximize, close). To make them smaller, try adding this to your `~/.config/gtk-3.0/gtk.css` file:

```css
/* Reduce the size of headerbar buttons in GNOME Terminal */
terminal-window headerbar button {
    min-width: 20px;
    min-height: 20px;
    padding: 2px;
    margin: 0;
}
```

Restart GNOME Shell (Alt+F2, then type `r` on Xorg) or log out and log back in for changes to take effect. Let me know if this doesn't work as expected!



--------------------------------------------------------------
---------------------------------------------------------------


