from setuptools import setup
import pydracula
setup_requires = ['setuptools']
try:
    setup(
        name=pydracula.__appname__.lower(),
        version=pydracula.__version__,
        author=pydracula.__author__,
        description=pydracula.__comment__,
        url=pydracula.__website__,
        license='GPLv3+',
        packages=['pydracula',
                  'pydracula.controllers',                  
                  'pydracula.controllers.main_window_decoration',                 
                  'pydracula.themes',
                  'pydracula.view',
                  'pydracula.model'],
        include_package_data=True,
        package_data={'pydracula': ['pydracula/assets/icons/*.svg',
                                 'pydracula/assets/icons/*.png'
                                 ]},
        setup_requires=setup_requires,
        entry_points={'gui_scripts': ['pydracula = pydracula.__main__:main']},
        keywords='pydracula whatsapp client web app',
        classifiers=[
            'Environment :: X11 Applications :: Qt',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Topic :: Office/Business',
            'Programming Language :: Python :: 3 :: Only'
        ]
    )
except Exception as e:
    print(e)
