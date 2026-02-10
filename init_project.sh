#!/usr/bin/env bash
set -e

PROJECT="multiagent-incident-bot"

mkdir -p $PROJECT/{agents,tools,configs,tests,docs}

touch $PROJECT/main.py
touch $PROJECT/requirements.txt
touch $PROJECT/.env.example
touch $PROJECT/.gitignore

touch $PROJECT/agents/{__init__.py,elastic_agent.py,analysis_agent.py,recommendation_agent.py,servicenow_agent.py,supervisor.py}
touch $PROJECT/tools/{__init__.py,elastic_tool.py,servicenow_tool.py}

echo "Project structure created" 
