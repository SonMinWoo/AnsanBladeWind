from setuptools import setup, find_packages



setup(

    name             = 'todoconsol',

    version          = '1.1.0',

    description      = 'Simple Todoconsol Program',

    license          = 'MIT',

    author           = 'Ansan Blade Wind',

    author_email     = 'hun97106@naver.com',

    url              = 'https://github.com/SonMinWoo/AnsanBladeWind',

    download_url     = 'https://github.com/SonMinWoo/AnsanBladeWind/archive/todoconsol-0.1.tar.gz',

    install_requires = [ ],

    packages         = find_packages(exclude = [ ]),

    keywords         = ['todoconsol', 'task manager'],

    python_requires  = '>=3',

    package_data     =  {'todoconsol' : ["LICENSE.md",'consolcolor']},

    py_modules       = ['todoconsol' ],

    entry_points     = {
                          'console_scripts' : [
                              'todoconsol = todoconsol:main',
                              ],
                          },
    zip_safe = False,

    classifiers      = [

        'Programming Language :: Python :: 3',

        'Programming Language :: Python :: 3.2',

        'Programming Language :: Python :: 3.3',

        'Programming Language :: Python :: 3.4',

        'Programming Language :: Python :: 3.5',

        'Programming Language :: Python :: 3.6'

        

    ]

)
