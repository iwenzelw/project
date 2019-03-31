import os

from .common import run_command, get_egg
from .output import output, WARN, ERROR
from .basket import Basket


def init(path):
    """
    Init [egg] command.

        Creates a directory and initial venv environment

    :param path:
    :return:
    """
    if path == '.' or os.path.exists(path) and os.listdir(path):
        output('Already exists an un-empty directory {0}'.format(path), ERROR)
        return
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    run_command('python3', '-m', 'venv', 'venv')


def search(egg):
    """
    Search hen packages, list 10 packages

    :param egg: hen name
    :return:
    """
    output(run_command('pip', 'search', egg))


def install(eggs, section):
    """
    Add eggs into given section

    :param eggs:
    :param section:
    :return:
    """
    basket = Basket()
    basket.open()
    if not eggs:
        _install_from_file(basket, section)
    else:
        _install_from_cli(basket, eggs, section)


def uninstall(eggs):
    """
    Remove eggs

    :param eggs:
    :return:
    """
    basket = Basket()
    basket.open()
    run_command('pip', 'uninstall', '-y', *eggs)
    basket.remove(eggs)
    basket.close()


def update():
    """
    Update all eggs

    :return:
    """
    basket = Basket()
    basket.open()
    all_outdated_eggs = _list_outdated_eggs()
    eggs = list(filter(lambda x: basket.section_of(x), all_outdated_eggs))
    if not eggs:
        output('Already latest', WARN)
        return
    run_command('pip', 'install', '-U', *eggs)
    results = _list_eggs()
    basket.update(eggs, results)
    basket.close()


def show(is_all=False):
    if is_all:
        lines = run_command('pip', 'list', '--format=columns').split('\n')[2:-1]
        eggs = '\n'.join(['{0} = {1}'.format(*get_egg(line)) for line in lines])
        output(eggs)
    else:
        basket = Basket()
        basket.show()


def _install_from_cli(basket, eggs, section):
    run_command('pip', 'install', *eggs)
    results = _list_eggs()
    section = section[0] if section else 'prod'
    basket.add(eggs, results, section)
    basket.close()


def _install_from_file(basket, section):
    sections = section if section else basket.sections()
    eggs = ['{0}=={1}'.format(key, value) for s in sections for key, value in basket.section(s).items()]
    run_command('pip', 'install', *eggs)


def _list_outdated_eggs():
    lines = _list_eggs(outdated=True)
    return [get_egg(line)[0] for line in lines.split('\n')[2:-1]]


def _list_eggs(outdated=False):
    args = ['pip', 'list', '--format=columns']
    if outdated:
        args.append('--outdated')
    results = run_command(*args)
    return results.lower()

