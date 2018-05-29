from setuptools import setup, find_packages



setup(

    name             = 'todoconsol',

    version          = '0.1',

    description      = 'The Open Source Ansan Blade Wind',

    author           = 'Moon Ki hun',

    author_email     = 'hun97106@naver.com',

    url              = 'https://github.com/SonMinWoo/AnsanBladeWind',

    download_url     = 'https://github.com/SonMinWoo/AnsanBladeWind/archive/Hanyang-1.0.tar.gz',

    install_requires = [ ],

    packages         = find_packages(exclude = [ ]),

    keywords         = ['todoconsol', 'task manager'],

    python_requires  = '>=3',

    package_data     =  {'todoconsol' : [ "LICENSE" ]},

    zip_safe=False,

    classifiers      = [

        'Programming Language :: Python :: 3',

        'Programming Language :: Python :: 3.2',

        'Programming Language :: Python :: 3.3',

        'Programming Language :: Python :: 3.4',

        'Programming Language :: Python :: 3.5',

        'Programming Language :: Python :: 3.6'

    ]

)
