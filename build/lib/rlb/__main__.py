#!/usr/bin/env python

import click
import pathlib
import time
from git import Repo
import os
from pyfiglet import Figlet

@click.command()
@click.option('--path', default=pathlib.Path().absolute(), required=True, help='Path to install, default is current Path')
@click.option('--typescript', default=False, type=bool, is_flag=True, help="Create a Typescript project")
@click.option('--project-name', required=True, type=str, help="Name of project")
def main(path, typescript, project_name):
    """Program to create a react project with less boilerplate"""
    f = Figlet(font='slant')
    if path:
        print(f.renderText('React Less Boilerplate'))
        if not typescript:
            try:
                click.secho("🔴  Not Installing Typescript", fg='red', bold=True)
                click.secho(f"✔ Project Name: {project_name}", fg='green', bold=True)
                time.sleep(1)
                path_to_create = os.path.join(path, project_name)
                click.secho(f'✔ Creating Project at: {str(path_to_create)}', fg='green')
                time.sleep(0.5)
                os.mkdir(path_to_create)
                clone = 'https://github.com/masonschafercodes/react-app-template-no-ts'
                Repo.clone_from(clone, pathlib.Path(path_to_create))
                time.sleep(1)
                os.chdir(path_to_create)
                click.secho('🔴  Removing Remote Origin', fg='red')
                time.sleep(1)
                os.system('git remote remove origin')
                time.sleep(1)
                click.secho('✔ Running Yarn Command', fg='green')
                time.sleep(1)
                os.system('yarn')
                click.secho("🎉   All Done!  🎉", fg='green', bold=True)
                click.secho("Next Steps!", fg='green', bold=True)
                click.secho(f"cd {project_name}", fg='blue', bold=True)
                click.secho(f"yarn run start", fg='blue', bold=True)
                os.system(f'cd {path}')
            except Exception as e:
                click.secho('‼ An Error has Occured - Please try again!', fg='red')
                print(e)

        if typescript:
            try:
                click.secho(f"✔ Installing Typescript", fg='green', bold=True)
                click.secho(f"✔ Project Name: {project_name}", fg='red', bold=True)
                time.sleep(1)
                path_to_create = os.path.join(path, project_name)
                click.secho(f'✔ Creating Project at: {str(path_to_create)}', fg='green')
                time.sleep(0.5)
                os.mkdir(path_to_create)
                clone = 'https://github.com/masonschafercodes/react-app-template-ts.git'
                Repo.clone_from(clone, pathlib.Path(path_to_create))
                time.sleep(1)
                os.chdir(path_to_create)
                click.secho('🔴  Removing Remote Origin', fg='red')
                time.sleep(1)
                os.system('git remote remove origin')
                time.sleep(1)
                click.secho('✔ Running Yarn Command', fg='green')
                time.sleep(1)
                os.system('yarn')
                click.secho("🎉   All Done!  🎉", fg='green', bold=True)
                click.secho("Next Steps!", fg='green', bold=True)
                click.secho(f"cd {project_name}", fg='blue', bold=True)
                click.secho(f"yarn run start", fg='blue', bold=True)
                os.system(f'cd {path}')
            except Exception as e:
                click.secho('‼ An Error has Occured - Please try again!', fg='red')
                print(e)

    else:
        click.secho("‼ Error: Please Provide a Path to Install!", fg='red', bold=True)

if __name__ == '__main__':
    main()