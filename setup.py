#!/usr/bin/env python
# encoding: utf-8

from setuptools import find_packages, setup

setup(
    name='eboshi',
    version='0.0.17',
    description='Azkaban CLI tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='wyukawa',
    author_email='wyukawa@gmail.com',
    url='https://github.com/wyukawa/eboshi',
    license='MIT',
    packages=find_packages(),
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Environment :: Console',
    ],
    install_requires=[
      'requests',
      'cliff'
    ],
    entry_points={
        'console_scripts': [
            'eboshi = eboshi.main:main'
        ],
        'eboshi': [
            'upload = eboshi.upload:Upload',
            'addSchedule = eboshi.add_schedule:Add_Schedule',
            'addCronSchedule = eboshi.add_cron_schedule:Add_Cron_Schedule',
            'listSchedules = eboshi.list_schedules:List_Schedules',
            'removeSchedule = eboshi.remove_schedule:Remove_Schedule',
            'removeAllSchedules = eboshi.remove_all_schedules:Remove_All_Schedules',
            'exec = eboshi.exec:Exec',
            'createProject = eboshi.create_project:Create_Project',
            'deleteProject = eboshi.delete_project:Delete_Project',
            'getSchedule = eboshi.get_schedule:Get_Schedule',
            'getMostRecentNextExecTime = eboshi.get_most_recent_next_exec_time:Get_Most_Recent_Next_Exec_Time',
            'fetchFlow = eboshi.fetch_flow:Fetch_Flow',
        ]
    },
)
