# SSH medic v1.0
import click
import os
import stat

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass

@main.command(hidden=True)
@click.pass_context
def help(ctx):
    print(ctx.parent.get_help())

@main.command()
def check():
    click.secho('Checking ssh dir and files...', fg='green')


if __name__ == '__main__':
    main()
