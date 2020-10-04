from __future__ import absolute_import
from distutils.core import setup

setup(
    name='Tic-Tac-Toe',
    version='0.8.0-dev',
    packages=['ttt'],
    entry_points={
        'jrb_board.games': 'ttt = ttt.board:Board',
    },
    install_requires=['six'],
    license='LICENSE',
    description="An implementation of Tic Tac Toe.",
)
