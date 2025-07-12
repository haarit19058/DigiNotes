Theme :  zero dark blue zen

fonts consolas

icons: A icons      atom icons

ctrl shift p 
package control


alt shift 2 : for two windows  
ctrl 1/2  to focus on the multiple open windows
alt 1/2 to open terminus in the windows or the panel


keybindings

```json
[
    // General
    { "keys": ["ctrl+shift+p"], "command": "show_overlay", "args": {"overlay": "command_palette"} },
    { "keys": ["ctrl+p"], "command": "show_overlay", "args": {"overlay": "goto", "text": "@"} },
    { "keys": ["ctrl+`"], "command": "show_panel", "args": {"panel": "console", "toggle": true} },

    // File Management
    { "keys": ["ctrl+n"], "command": "new_file" },
    { "keys": ["ctrl+o"], "command": "prompt_open_file" },  // Open file
    { "keys": ["ctrl+k", "ctrl+o"], "command": "prompt_open_folder" },  // Open folder
    { "keys": ["ctrl+s"], "command": "save" },
    { "keys": ["ctrl+w"], "command": "close" },
    { "keys": ["ctrl+shift+t"], "command": "reopen_last_file" },

    // Editing
    { "keys": ["ctrl+x"], "command": "cut" },
    { "keys": ["ctrl+c"], "command": "copy" },
    { "keys": ["alt+up"], "command": "swap_line_up" },
    { "keys": ["alt+down"], "command": "swap_line_down" },
    { "keys": ["shift+alt+down"], "command": "duplicate_line" },
    { "keys": ["ctrl+shift+k"], "command": "run_macro_file", "args": {"file": "Packages/Default/Delete Line.sublime-macro"} },
    { "keys": ["ctrl+enter"], "command": "insert", "args": {"characters": "\n"} },
    { "keys": ["ctrl+shift+enter"], "command": "insert", "args": {"characters": "\n"} },
    { "keys": ["ctrl+/"], "command": "toggle_comment", "args": {"block": false} },
    { "keys": ["shift+alt+a"], "command": "toggle_comment", "args": {"block": true} },
    { "keys": ["ctrl+shift+l"], "command": "find_all_under" },  // Select all occurrences of the selected word

    // Navigation
    { "keys": ["ctrl+g"], "command": "show_overlay", "args": {"overlay": "goto", "text": ":"} },
    { "keys": ["ctrl+shift+o"], "command": "show_overlay", "args": {"overlay": "goto", "text": "@"} },
    { "keys": ["f12"], "command": "goto_definition" },
    { "keys": ["alt+f12"], "command": "show_overlay", "args": {"overlay": "goto", "text": "@"} },
    { "keys": ["f8"], "command": "next_result" },
    { "keys": ["shift+f8"], "command": "prev_result" },

    // Multi-Cursor and Selection
    { "keys": ["ctrl+alt+up"], "command": "select_lines", "args": {"forward": false} },
    { "keys": ["ctrl+alt+down"], "command": "select_lines", "args": {"forward": true} },
    { "keys": ["ctrl+shift+up"], "command": "select_lines", "args": {"forward": false} },  // Add cursor above
    { "keys": ["ctrl+shift+down"], "command": "select_lines", "args": {"forward": true} },  // Add cursor below
    { "keys": ["shift+alt+i"], "command": "split_selection_into_lines" },
    { "keys": ["ctrl+d"], "command": "find_under_expand" },
    { "keys": ["ctrl+u"], "command": "soft_undo" },

    // Search and Replace
    { "keys": ["ctrl+f"], "command": "show_panel", "args": {"panel": "find"} },
    { "keys": ["ctrl+h"], "command": "show_panel", "args": {"panel": "replace"} },
    { "keys": ["ctrl+shift+f"], "command": "show_panel", "args": {"panel": "find_in_files"} },
    { "keys": ["ctrl+shift+h"], "command": "show_panel", "args": {"panel": "replace", "in_selection": true} },

    // View and Appearance
    { "keys": ["ctrl+b"], "command": "toggle_side_bar" },  // Toggle side bar
    { "keys": ["ctrl+="], "command": "increase_font_size" },
    { "keys": ["ctrl+-"], "command": "decrease_font_size" },
    { "keys": ["f11"], "command": "toggle_full_screen" },
    { "keys": ["ctrl+k", "z"], "command": "toggle_distraction_free" },

    // Debugging (if installed via a plugin like SublimeGDB or Terminus)
    { "keys": ["f5"], "command": "build" },
    { "keys": ["f10"], "command": "step_over" },
    { "keys": ["f11"], "command": "step_into" },
    { "keys": ["shift+f11"], "command": "step_out" },
    { "keys": ["f9"], "command": "toggle_breakpoint" },



    { "keys": ["alt+1"], "command": "toggle_terminus_panel",
     "args": {
        "panel_name": "first-panel",
        // "panel_position": "right"
        },
    },

    // { "keys": ["alt+2"], "command": "toggle_terminus_panel", "args": {
    //     "panel_name": "other-panel"
    // }, },

    {
        "keys": ["f11"], "command": "toggle_full_screen"  // Toggle full screen mode
    },


    {
    "keys": ["alt+2"],
    "command": "terminus_open",
    "args": {
        "cwd": "${file_path:${folder}}"
    }
}
]

```



settings
```json
{
    "font_face": "Consolas",       
    "font_size": 13,               
    "caret_extra_top":1,
    "caret_extra_bottom":1,
    "caret_extra_width":0,
    "caret_style":"smooth",
    
    "theme": "Adaptive.sublime-theme",
    "color_scheme": "Dark PRO Blue Zen.sublime-color-scheme",
    "index_files": true,

    "auto_complete": false,
    "auto_complete_triggers": [],
    "auto_complete_commit_on_tab": false,
    "spell_check": false,
    "show_hover": false,
    "show_signature_help": false,
    "inlay_hints_enabled": false,
    "show_definitions": false,


    "ignored_packages":
    [
		"Vintage",
    ],
}

```


termux
```json
{
	"view_settings": {
		"font_size":12

        // these are extra view settings which are passed to the terminus_view,
        // you could change settings like "font_face", "font_size" and paddings.
        // you should also specify these settings in the syntax specfic file
        // "Terminus View.sublime-settings".
    },
}
```


