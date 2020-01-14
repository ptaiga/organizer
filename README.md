# Simple organizer app

## To-do list:

### 5th stage. Part 2 ###
(_ver. 0.4.9 -> 0.5.0_: progressive features)

**Features**:
 - [ ] Import data from JSON
 - [ ] Sharing projects with other users
 - [ ] Visitor's statistics
 - [ ] Automatic register new users and send them email
 - [ ] Extend time for snooze tasks (to week, to deadline)
 - [ ] Variable for auto-naming of repeated tasks
 - [ ] In Week folder separate tasks for tomorrow
 - [ ] Task assigment date in addition to the deadline
 - [ ] Optimize date visualization: 
   - [ ] weekday for tasks in current week 
   - [ ] hide year for current year tasks
   - [x] by default 20:59 -> 20:00 (for reduce text)
 - [ ] Tomorrow tasks in Today with hide/show button
 - [ ] Categorize task in Week by day of week (consider repeating tasks)
 - [ ] Beauty placeholder in empty Today-folder: for example, "You're great!" or big green tick

**Profile**:
 - [ ] Checkbox in profile to subscribe/unsubscribe today notification
 - [ ] Profile page with all user's data
 - [ ] Ability to change email
 - [ ] Link to confirm email
 - [ ] Checkbox for random tasks in daily email
 - [ ] Choose number of random tasks in daily email
 
 **UX/UI**:
 - [ ] Turn on/off sidebar save to cookies
 - [ ] Wrap/unwrap block with active projects in sidebar
 
 **Bugs**:
 - [ ] Changing task from Today folder redirect to task's project
 - [ ] Link "organizer/export/" don't work properly
 - [ ] Sort doesn't work in Week
 - [x] Incorrect work of week-folder for weekend

---

### 5th stage. Part 1 ###
(_ver. 0.4.1 -> 0.4.8_: release progressive features from __Jul 21, 2018__ to __Oct 29, 2018__)

**Features**:
 - [x] Set time to 20:59 if add date without time
 - [x] In Week folder sort tasks by due_date
 - [x] Add random task in today email
 - [x] Add repeating every two days
 - [x] Subject in message begin with capitalize letter
 - [x] Link to organizer in email massage about today tasks
 - [x] Email notification about today tasks
 - [x] Separate application for user profile

**Refactoring**:
 - [x] Review projects_change and projects_rename view

**Bugs**:
 - [x] Crash introduction page style when use https
 - [x] Week counts next Sunday tasks
 - [x] Url 'organizer/asdf' go to Inbox with "Asdf" header
 - [x] When go into hidden project look at "View hidden projects" link
 - [x] Instead of renaming the project is hidden
 - [x] Close a task in Today folder go to project folder of the task or Inbox
 - [x] Task snooze but continue to count near the folder
 - [x] Repeat tasks 500 Server Error without due_date
 - [x] Error with closing project's task in today or week folder ('url projects/0/task_apply not found')

**Useful links**:
 + https://ru.stackoverflow.com/questions/17991/django-%D0%B8-cron
 + https://help.pythonanywhere.com/pages/ScheduledTasks/

---

### 4th stage ###
(_ver. 0.3.1 -> 0.4.0_: continue to develop)

**Features**:
 - [x] View projects and tasks data in txt and html
 - [x] Export data in JSON
 - [x] Show tasks properties (hide it by default)
 - [x] Priority of tasks (A, B and C)
 - [x] Snooze tasks (ability to temporarily hide tasks)
 - [x] Pereodical tasks (https://dateutil.readthedocs.io)
 - [x] Render "About" page from README.md (https://github.com/Python-Markdown/markdown)
 - [x] Active http-links in comments (https://docs.djangoproject.com/en/dev/ref/templates/builtins/#urlize)

**Bugs**:
 - [x] Sorting return to default after something operations. Maybe to use save in user's model setting of sort and also different other.
 - [x] Today, Week -> Task viewing back transition leads to project of task
 - [x] DateTimeField Task.due_date received a naive datetime while time zone support is active.
 - [x] There is no options to restore deleted projects
 - [x] Into deleted projects showing deleted tasks (not active tasks by default)

**Useful links about exporting data**:
  https://docs.djangoproject.com/en/2.0/ref/request-response/#telling-the-browser-to-treat-the-response-as-a-file-attachment
  https://codebeautify.org/jsonviewer
  https://docs.djangoproject.com/en/2.0/howto/outputting-pdf/
  https://stackoverflow.com/questions/41958335/django-render-a-txt-file-with-linebreaks

---

### Third stage ###
**Progressive improvement** (_ver. 0.2.1 -> 0.3.0_: still without use of JS).

**Backend**:
 - [x] Send message
 - [x] Registration page
 - [x] Weekly tasks
 - [x] Today tasks
 - [x] After logout goto index page
 - [x] Last edit time for comments
 - [x] Line breaks in comments
 - [x] Edit comments text
 - [x] Hide the comments instead of deleting

**Frontend**:
 - [x] Sort tasks by publication date (newest or latest)
 - [x] Highlighting (red color) of overdue tasks
 - [x] Numbers of comments to task
 - [x] Empty data input verification
 - [x] Checkboxes for tasks instead radiobuttons
 - [x] Change project of task
 - [x] View number of tasks for every project in sidebar

---

### Second stage ###
**Progressive development** (_ver. 0.1.1 -> 0.2.0_).

Frontend:
  - Layout:
    - [x] Base html-structure of the page
    - [x] Mobile first
    - [x] Responsive design
    - [x] Collapse navbar
    - [x] Turn on/off sidebar
    - [x] Area for comments
    - [x] Refactoring
    - [x] Flexibility for aside area

#### Useful resources:

Grid Layout:
 + https://medium.com/web-standards/responsive-grid-system-89d07e48a564
 + Screencast about base of CSS Grid (from WebDesign Master) - https://www.youtube.com/watch?v=-fDqBEjfzGo
 + https://medialoot.com/blog/how-to-create-a-responsive-navigation-menu-using-only-css/

 Flexbox:
 + https://tuhub.ru/posts/flexbox-complete-guide (https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
 + http://css-live.ru/articles/vizualnoe-rukovodstvo-po-svojstvam-flexbox-iz-css3.html -> http://html5.by/blog/flexbox/
 + http://css-live.ru/articles/flex-grow-strannyj-tak-li-eto.html -> https://drafts.csswg.org/css-flexbox/#flexibility

Backend (Done, v0.1.1):
  - [x] Refactoring
  - [x] User authorization
  - [x] Comments
  - [x] History
  - [x] Tasks deadline time
  - [x] Completeness flag for tasks/projects
  - [x] Inbox
  - [x] Rename projects/tasks

---

### First stage ###
**Working prototype** (_ver. 0.1.0_: provides minimal, but sufficient opportunities for work):
- [x] Add projects
- [x] Add tasks
- [x] Delete projects
- [x] Delete tasks
- [x] Minimalistic design

#### List of used sources
**Backend**:
 + https://djangoproject.com - Django documentation

**Layout**:
 + https://medium.com/flexbox-and-grids/css-flexbox-grid-layout-how-to-approach-css-layouts-in-2017-and-beyond-685deef03e6c
 + https://developer.mozilla.org/en-US/docs/Web/HTML/Element - HTML5 tags description



