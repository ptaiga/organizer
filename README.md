# Simple organizer app

## To-do list:

### 4th stage ###
(_ver. 0.3.1 -> 0.4.0_: continue to develop)

 - [ ] Choose framework

**Features**:
 - [ ] Common project for several users
 - [ ] Export data in different format (pdf, html, txt)
 - [ ] Prioritization of tasks (A, B and C)
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



