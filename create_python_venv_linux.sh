if [ ${0##*/} == ${BASH_SOURCE[0]##*/} ]; then 
    echo "WARNING"
    echo "This script is not meant to be executed directly!"
    echo "Use this script only by sourcing it."
    echo
    exit 1
fi
python3.10 -m venv .linux_env && . ./.linux_env/bin/activate && pip install -r requirements.txt
