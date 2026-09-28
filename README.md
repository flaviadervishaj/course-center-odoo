# Course Center

An academic Odoo 17 module for managing a course center. It models courses, categories, groups, instructors, students, sessions, enrollments, assignments, submissions, attendance, invoices, payments, discounts, and certificates.

## What is in this repository

- Course groups connect a course with an instructor; sessions can be assigned to a group and room.
- Enrollments connect students to groups and record status, payment plan, and pricing fields.
- Assignments and submissions record coursework and grades.
- Attendance, invoices, payments, discount rules, and certificates have their own models and views.
- Menus organize these records into People, Courses, Management, Finance, and Configuration.

This repository contains the Odoo addon source. It does not contain a hosted demo, a database, or sample accounts. The public snapshot includes a role field on users, but does not include Odoo security groups or model access CSV files; it should be treated as an academic development project rather than a ready-to-deploy multi-user system.

## Technology

Odoo 17, Python, PostgreSQL, and XML views.

## Local setup

1. Install Odoo 17 with PostgreSQL and create a development database.
2. Clone this repository into a directory named `course_center` inside a custom addons directory.
3. Add the **parent** custom addons directory to Odoo's `addons_path` and restart Odoo.
4. In developer mode, update the Apps list, then search for and install **Course Center** using an administrator account.

The addon declares only Odoo's `base` module as a dependency. Before using it with non-administrator accounts, define and test appropriate Odoo groups, access controls, and record rules for student and instructor data.

## Structure

- `__manifest__.py` lists the module metadata and loaded views.
- `models/` contains the course center data models.
- `views/` contains form, list, and menu definitions.

No automated install or browser test is included in this repository. Validate the addon in a separate Odoo 17 development database before using it with real data.
