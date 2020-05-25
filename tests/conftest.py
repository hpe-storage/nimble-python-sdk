# pytest_plugins = 'pytest_session2file'
# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pytest Plugin that save failure or test session information to a file pass as
a command line argument to pytest.

It put in a file exactly what pytest return to the stdout.

To use it :
Put this file in the root of tests/ edit your conftest and insert in the top
of the file :

    pytest_plugins = 'pytest_session_to_file'

Then you can launch your test with the new option --session_to_file=like this :

    py.test --session_to_file=FILENAME
Or :
    py.test -p pytest_session_to_file --session_to_file=FILENAME


Inspire by _pytest.pastebin
Ref: https://github.com/pytest-dev/pytest/blob/master/_pytest/pastebin.py

Version : 0.1
Date : 30 sept. 2015 11:25
Copyright (C) 2015 Richard Vézina <ml.richard.vezinar @ gmail.com>
Licence : Public Domain
"""

import pytest
import tempfile


def pytest_addoption(parser):
    group = parser.getgroup("terminal reporting")
    group._addoption('--session_to_file', action='store', metavar='path',
                     default='tests//logs//pytest_session.log',
                     help="Save to file the pytest session information")


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    tr = config.pluginmanager.getplugin('terminalreporter')
    # if no terminal reporter plugin is present, nothing we can do here;
    # this can happen when this function executes in a slave node
    # when using pytest-xdist, for example
    if tr is not None:
        config._pytestsessionfile = tempfile.TemporaryFile('w+')
        oldwrite = tr._tw.write

        def tee_write(s, **kwargs):
            oldwrite(s, **kwargs)
            config._pytestsessionfile.write(str(s))
        tr._tw.write = tee_write


def pytest_unconfigure(config):
    if hasattr(config, '_pytestsessionfile'):
        # get terminal contents and delete file
        config._pytestsessionfile.seek(0)
        sessionlog = config._pytestsessionfile.read()
        config._pytestsessionfile.close()
        del config._pytestsessionfile
        # undo our patching in the terminal reporter
        tr = config.pluginmanager.getplugin('terminalreporter')
        del tr._tw.__dict__['write']
        # write summary
        create_new_file(config=config, contents=sessionlog)


def create_new_file(config, contents):
    """
    Creates a new file with pytest session contents.
    :contents: paste contents
    :returns: url to the pasted contents
    """
    # import _pytest.config
    # path = _pytest.config.option.session_to_file
    # path = 'pytest_session.txt'
    try:
        path = config.option.session_to_file
        with open(path, 'w') as f:
            f.writelines(contents)
    except Exception:
        pass


def pytest_terminal_summary(terminalreporter):
    import _pytest.config
    tr = terminalreporter
    if 'failed' in tr.stats:
        for rep in terminalreporter.stats.get('failed'):
            try:
                rep.longrepr.reprtraceback.reprentries[-1].reprfileloc
            except AttributeError:
                tr._getfailureheadline(rep)
            tw = _pytest.config.create_terminal_writer(terminalreporter.config,
                                                       stringio=True)
            rep.toterminal(tw)
            s = tw.stringio.getvalue()
            assert len(s)
            create_new_file(config=_pytest.config, contents=s)
