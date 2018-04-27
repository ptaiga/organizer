### Tasks for next (> v0.3) stage of project

#### General features

 - [ ] Tabbed interface
 - [ ] Calendars for visualization of activity by projects and tasks (timeline)
 - [ ] Check time
 - [ ] Oppotunity for paid-features API
 - [ ] Fitness tracking
 - [ ] Export/Import data in different format
 - [ ] Localization (choose language)
 - [ ] Offline mode (local storage?)
 - [ ] Fast notes
 - [ ] Diary
 - [ ] Tags
 - [ ] Manually estimating duration of tasks
 - [ ] Estimating duration of projects
 - [ ] Separate application for profile
 - [ ] Pereodical tasks
 - [ ] Local time for users
 - [ ] Active http-links in comments
 - [ ] Choose framework
 - [ ] Ajax for base operations
 - [ ] Drag'n'drop for task and project location
 - [ ] Different scrollbars for project and task areas
 - [ ] Custom, accurate and minimal width scrollbar
 - [ ] Manualy change width of projects bar
 - [ ] Remember settings (cookie or local storage)
 - [ ] Subprojects (or nesting)
 - [ ] Subtasks (or nesting)
 - [ ] Prioritization of tasks (A, B and C)
 - [ ] Calendar: comfortable popup (or something other)
 - [ ] Cover code with test
 - [ ] Render "About" page from README.md
 - [ ] Common project for several users

#### Bugs

- DateTimeField Task.due_date received a naive datetime while time zone support is active.
- Today, Week -> Task viewing back transition leads to project of task
- Into deleted projects showing deleted tasks (not active tasks by default)
- There is no options to restore deleted projects
- Sorting return to default after something operations. Maybe to use save in user's model setting of sort and also different other.
