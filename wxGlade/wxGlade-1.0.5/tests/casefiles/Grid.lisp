;;; generated by wxGlade
;;;

(asdf:operate 'asdf:load-op 'wxcl)
(use-package "FFI")
(ffi:default-foreign-language :stdc)


;;; begin wxGlade: dependencies
(use-package :wxCL)
(use-package :wxColour)
(use-package :wxEvent)
(use-package :wxEvtHandler)
(use-package :wxFrame)
(use-package :wxGrid)
(use-package :wxSizer)
(use-package :wxWindow)
(use-package :wx_main)
(use-package :wx_wrapper)
;;; end wxGlade

;;; begin wxGlade: extracode
;;; end wxGlade


(defclass MyFrame()
        ((top-window :initform nil :accessor slot-top-window)
        (sizer-1 :initform nil :accessor slot-sizer-1)
        (grid-1 :initform nil :accessor slot-grid-1)))

(defun make-MyFrame ()
        (let ((obj (make-instance 'MyFrame)))
          (init obj)
          (set-properties obj)
          (do-layout obj)
          obj))

(defmethod init ((obj MyFrame))
"Method creates the objects contained in the class."
        ;;; begin wxGlade: MyFrame.__init__
        (setf (slot-top-window obj) (wxFrame_create nil wxID_ANY "" -1 -1 -1 -1 wxDEFAULT_FRAME_STYLE))
        (wxFrame_SetTitle (slot-top-window obj) "frame_1")
        
        (setf (slot-sizer-1 obj) (wxBoxSizer_Create wxVERTICAL))
        
        (setf (slot-grid-1 obj) (wxGrid_Create (slot-top-window obj) wxID_ANY -1 -1 -1 -1 wxWANTS_CHARS))
        (wxGrid_CreateGrid (slot-grid-1 obj) 2 2 0)
        (wxGrid_SetGridLineColour (slot-grid-1 obj) (wxColour:wxColour_CreateFromStock 255, 0, 0))
        (wxGrid_SetLabelBackgroundColour (slot-grid-1 obj) (wxColour:wxColour_CreateFromStock 216, 191, 216))
        (wxGrid_SetColLabelValue (slot-grid-1 obj) 0 "Column A")
        (wxGrid_SetColLabelValue (slot-grid-1 obj) 1 "Column B")
        (wxWindow_SetBackgroundColour (slot-grid-1 obj) (wxColour_CreateRGB 0, 255, 255))
        (wxGrid_SetRowLabelValue (slot-(slot-grid-1 obj) obj) 0, "Row 1")
        (wxGrid_SetCellValue (slot-(slot-grid-1 obj) obj) 0, 0, "1")
        (wxSizer_AddWindow (slot-sizer-1 obj) (slot-grid-1 obj) 1 wxEXPAND 0 nil)
        
        (wxWindow_SetSizer (slot-top-window obj) (slot-sizer-1 obj))
        (wxSizer_Fit (slot-sizer-1 obj) (slot-top-window obj))
        
        (wxFrame_layout (slot-frame-1 self))

        (wxEvtHandler_Connect (slot-top-window obj) obj.grid-1 (expwxEVT_GRID_CMD_CELL_LEFT_CLICK)
        (wxClosure_Create #'myEVT_GRID_CELL_LEFT_CLICK obj))
        ;;; end wxGlade
        )

(defun myEVT_GRID_CELL_LEFT_CLICK (function data event) ;;; wxGlade: MyFrame.<event_handler>
        (print "Event handler 'myEVT_GRID_CELL_LEFT_CLICK' not implemented!")
        (when event
                (wxEvent:wxEvent_Skip event)))

;;; end of class MyFrame


