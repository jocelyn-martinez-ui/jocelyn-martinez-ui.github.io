window.PORTFOLIO_SYSTEMS = [
  {
    "id": "imhere",
    "name": "ImHere",
    "path": "ImHere-case-study/imhere-case-study.html",
    "type": "Jakarta Sans + IBM Plex Mono",
    "ui": "Dense but readable faculty tables; a narrow student workspace; a correction form that compares old and proposed states before committing. A record, session and review request remain separate concepts.",
    "motion": "150 ms control feedback. A changed view moves focus to its heading. Confirmation is announced in a status region; no celebratory animation accompanies a consequential record change.",
    "tokens": {
      "--ink": "#142b49",
      "--accent": "#164b8d",
      "--paper": "#f2f5f9",
      "--surface": "#fff",
      "--tint": "#e6eef9",
      "--line": "#d9e2ec",
      "--muted": "#526780",
      "--signal": "#ec9a51",
      "--sans": "'Plus Jakarta Sans',sans-serif",
      "--display": "'Plus Jakarta Sans',sans-serif",
      "--radius": "8px"
    },
    "flow": [
      "Open class session",
      "Check in or request review",
      "Faculty reads context",
      "Explain correction",
      "Inspect shared record"
    ],
    "states": [
      [
        "Open session",
        "Student can enter the verification demonstration."
      ],
      [
        "Closed session",
        "Check-in is disabled; the correction path remains available."
      ],
      [
        "Needs review",
        "Written student context accompanies the record."
      ],
      [
        "Correction draft",
        "No record change until the reason is saved; cancellation leaves it intact."
      ],
      [
        "Recorded change",
        "Previous state, new state, actor and reason appear together."
      ]
    ]
  },
  {
    "id": "holland",
    "name": "Holland Walking Tour",
    "path": "Holland-Walking-Tour-site/holland-walking-tour-case-study.html",
    "type": "DM Serif + Source Sans 3",
    "ui": "Three visitor navigation choices: Find a walk, My walk and Help. A separate content studio holds editorial tools. Selection checkboxes update the pending itinerary before the visitor starts.",
    "motion": "Quiet 150 ms feedback with an explicit quiet-interface preference. Large-text changes are immediate. Pause keeps the current story; previous and next stay in stable positions.",
    "tokens": {
      "--ink": "#233f42",
      "--accent": "#176369",
      "--paper": "#f6f9f8",
      "--surface": "#fff",
      "--tint": "#e4efeb",
      "--line": "#c9d9d3",
      "--muted": "#506663",
      "--signal": "#eed785",
      "--sans": "'Source Sans 3',Arial,sans-serif",
      "--display": "'DM Serif Display',Georgia,serif",
      "--radius": "14px",
      "--guide-size": "18px"
    },
    "flow": [
      "Choose a walk",
      "Review selected stories",
      "Begin deliberately",
      "Read, pause or continue",
      "Finish at your pace"
    ],
    "states": [
      [
        "No selected stories",
        "Explain the next step and disable preview until one is selected."
      ],
      [
        "Walk not started",
        "Show a route-selection action rather than invented progress."
      ],
      [
        "Paused",
        "Keep the current story; stop next/previous advancement until resumed."
      ],
      [
        "Larger text",
        "Increase reading size without hiding navigation."
      ],
      [
        "Editorial draft",
        "Require the content contract before marking ready for review."
      ]
    ]
  },
  {
    "id": "aurea",
    "name": "Áurea",
    "path": "aurea.html",
    "type": "Italiana + DM Sans",
    "ui": "A database first: persistent search, family filters, an alphabetic note index, card/list results, a structured dossier and a two-perfume comparison. Each active filter can be removed independently.",
    "motion": "Subtle 160 ms border and color changes. Comparison feedback is written and announced. No floating bottle animation or parallax competes with information retrieval.",
    "tokens": {
      "--ink": "#302529",
      "--accent": "#713c46",
      "--paper": "#fcfaf5",
      "--surface": "#fff",
      "--tint": "#efe4db",
      "--line": "#dcd3ca",
      "--muted": "#73615f",
      "--signal": "#e7d875",
      "--sans": "'DM Sans',sans-serif",
      "--display": "'Italiana',Georgia,serif",
      "--radius": "4px"
    },
    "flow": [
      "Search or choose a note",
      "Refine a result set",
      "Inspect a perfume record",
      "Compare two profiles",
      "Save or record a wear note"
    ],
    "states": [
      [
        "No results",
        "Keep the selected filters visible and removable one at a time."
      ],
      [
        "One selected",
        "Ask for one more perfume before showing a comparison."
      ],
      [
        "Two selected",
        "Expose a readable side-by-side record."
      ],
      [
        "Third selection",
        "Offer replacement of either existing perfume, or cancel."
      ],
      [
        "Empty journal",
        "Prompt for an impression; never generate a fake personal review."
      ]
    ]
  },
  {
    "id": "loopline",
    "name": "Loopline",
    "path": "loopline.html",
    "type": "Barlow Condensed + Space Grotesk",
    "ui": "A practical partner desk with eligibility, description, timing and review. A confirmed sample remains editable; an edit is a draft until saved. The receipt distinguishes a preferred window from an arranged pickup.",
    "motion": "Quick 120 ms control feedback. Progress changes only after a successful step. The simulated journey advances manually; no fake real-time pulsing location dot.",
    "tokens": {
      "--ink": "#173629",
      "--accent": "#173629",
      "--paper": "#f4f0e8",
      "--surface": "#fffdf8",
      "--tint": "#bddccb",
      "--line": "#bdc6b7",
      "--muted": "#435b4b",
      "--signal": "#f4c95d",
      "--sans": "'Space Grotesk',sans-serif",
      "--display": "'Barlow Condensed',sans-serif",
      "--radius": "0px"
    },
    "flow": [
      "Confirm eligibility",
      "Describe food and containers",
      "Choose a preferred window",
      "Review details",
      "Revise before coordination"
    ],
    "states": [
      [
        "Eligibility unknown",
        "Pause the flow and direct the operator to their organization."
      ],
      [
        "Invalid quantity",
        "Require a whole number within the sample range."
      ],
      [
        "Review pending",
        "State that no pickup has been booked."
      ],
      [
        "Editing",
        "Keep the last record intact until save; offer cancel."
      ],
      [
        "Revised",
        "Update one record and increment its visible revision."
      ]
    ]
  },
  {
    "id": "nutriva",
    "name": "Nutriva",
    "path": "nutriva-portfolio-prototype/nutriva.html",
    "type": "DM Sans + friendly rounded accents",
    "ui": "Pantry corrections, ranked meal suggestions, a flexible plan and a derived grocery list share state. Every missing item names the planned meals that require it. A removed pantry ingredient has an undo path.",
    "motion": "160 ms button and selection feedback. Update results immediately after a pantry edit; announce the change without animating or reordering while someone is typing.",
    "tokens": {
      "--ink": "#203e2b",
      "--accent": "#294b31",
      "--paper": "#f7f9f3",
      "--surface": "#fff",
      "--tint": "#e8efdc",
      "--line": "#d8e0cf",
      "--muted": "#566951",
      "--signal": "#f5db54",
      "--sans": "'DM Sans',sans-serif",
      "--display": "'Nunito Sans',sans-serif",
      "--radius": "16px"
    },
    "flow": [
      "Review pantry",
      "Choose a meal by fit",
      "Add to flexible plan",
      "Inspect missing ingredients",
      "Correct or undo inventory"
    ],
    "states": [
      [
        "Uncertain inventory",
        "Keep suggestions separate until the user confirms them."
      ],
      [
        "Pantry edit",
        "Update related suggestions and missing items."
      ],
      [
        "Accidental removal",
        "Offer undo in the pantry view."
      ],
      [
        "No planned meals",
        "Explain how to start a grocery list."
      ],
      [
        "Nothing missing",
        "State that listed names are covered; quantities still need checking."
      ]
    ]
  },
  {
    "id": "novella",
    "name": "Novella",
    "path": "Novella-interactive.html",
    "type": "Newsreader + Libre Baskerville",
    "ui": "Mood and genre filters remain optional. Blind reading is a secondary path with a reveal action. Book details can directly save a title to Want to read, Reading or Finished; passages keep their source and support undo.",
    "motion": "Gentle 180 ms color changes with no autoplay page turning. Reader controls respond immediately. Changing a shelf announces the result without a streak, score or celebration.",
    "tokens": {
      "--ink": "#272525",
      "--accent": "#6f3338",
      "--paper": "#faf9f6",
      "--surface": "#fff",
      "--tint": "#f1e9e6",
      "--line": "#dcd7d1",
      "--muted": "#696463",
      "--signal": "#c0ccec",
      "--sans": "'Inter',sans-serif",
      "--display": "'Newsreader',Georgia,serif",
      "--radius": "0px"
    },
    "flow": [
      "Choose a mood or an excerpt",
      "Meet the book",
      "Read comfortably",
      "Place it on a shelf",
      "Keep or restore a passage"
    ],
    "states": [
      [
        "No matching titles",
        "Offer a clear filter reset."
      ],
      [
        "Blind excerpt",
        "Keep the title hidden until the reader chooses reveal."
      ],
      [
        "Shelf chosen",
        "Save the book and show the current reading state."
      ],
      [
        "Reader limits",
        "Disable type controls at the defined size bounds."
      ],
      [
        "Passage removed",
        "Offer undo and restore the original source association."
      ]
    ]
  }
];
