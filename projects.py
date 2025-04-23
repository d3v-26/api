import json
import os

PROJECTS_FILE = 'projects.json'


def load_projects():
    if not os.path.exists(PROJECTS_FILE):
        return []
    with open(PROJECTS_FILE, 'r') as file:
        return json.load(file)


def save_projects(projects):
    with open(PROJECTS_FILE, 'w') as file:
        json.dump(projects, file, indent=2)


def insert_project():
    project = {
        "title": input("Title: "),
        "description": input("Description: "),
        "technologies": input("Technologies (comma-separated): ").split(','),
        "links": {
            "github": input("GitHub URL: "),
            "live": input("Live URL (leave blank if none): ")
        },
        "tags": input("Tags (comma-separated): ").split(',')
    }
    projects = load_projects()
    projects.append(project)
    save_projects(projects)
    print("Project inserted.")


def update_project():
    title = input("Enter the title of the project to update: ")
    projects = load_projects()
    for project in projects:
        if project["title"].lower() == title.lower():
            print("Found project. Leave fields blank to keep existing values.")
            project["description"] = input(f"New Description (current: {project['description']}): ") or project["description"]
            tech_input = input(f"New Technologies (comma-separated) (current: {project['technologies']}): ")
            if tech_input:
                project["technologies"] = tech_input.split(',')
            github = input(f"New GitHub URL (current: {project['links']['github']}): ")
            if github:
                project["links"]["github"] = github
            live = input(f"New Live URL (current: {project['links'].get('live', '')}): ")
            if live:
                project["links"]["live"] = live
            tag_input = input(f"New Tags (comma-separated) (current: {project['tags']}): ")
            if tag_input:
                project["tags"] = tag_input.split(',')
            save_projects(projects)
            print("Project updated.")
            return
    print("Project not found.")


def delete_project():
    title = input("Enter the title of the project to delete: ")
    projects = load_projects()
    updated_projects = [p for p in projects if p["title"].lower() != title.lower()]
    if len(updated_projects) == len(projects):
        print("No project found with that title.")
    else:
        save_projects(updated_projects)
        print("Project deleted.")


def main():
    print("Choose an action: [1] Insert  [2] Update  [3] Delete")
    choice = input("Your choice: ")

    if choice == '1':
        insert_project()
    elif choice == '2':
        update_project()
    elif choice == '3':
        delete_project()
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
