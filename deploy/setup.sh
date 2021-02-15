#!/usr/bin/env bash

set -Eeuo pipefail
trap cleanup SIGINT SIGTERM ERR EXIT

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

usage() {
  cat <<EOF
Usage: $(basename "${BASH_SOURCE[0]}") [-h] [-v] [-f] -p param_value arg1 [arg2...]

Script description here.

Available options:

-h, --help      Print this help and exit
-v, --verbose   Print script debug info
-f, --flag      Some flag description
-p, --param     Some param description
EOF
  exit
}

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # script cleanup here
}

setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOFORMAT='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOFORMAT='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}

msg() {
  echo >&2 -e "${1-}"
}

die() {
  local msg=$1
  local code=${2-1} # default exit status 1
  msg "$msg"
  exit "$code"
}

parse_params() {
  # default values of variables set from params
  flag=0
  param=''

  while :; do
    case "${1-}" in
    -h | --help) usage ;;
    -v | --verbose) set -x ;;
    --no-color) NO_COLOR=1 ;;
    -f | --flag) flag=1 ;; # example flag
    # -p | --rooot) # example named parameter
    #   param="${2-}"
    #   shift
    #   ;;
    -?*) die "Unknown option: $1" ;;
    *) break ;;
    esac
    shift
  done

  args=("$@")

  # check required params and arguments
#   [[ -z "${param-}" ]] && die "Missing required parameter: param"
#   [[ ${#args[@]} -eq 0 ]] && die "Missing script arguments"

  return 0
}

parse_params "$@"
setup_colors

cd ..
WD=$PWD

sudo apt-get install python3-venv
sudo apt install python3-pip

cd $WD/pass_go
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env.example .env

cd $WD/rtc_service
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env.example .env


sudo apt -y update
sudo apt install -y supervisor
sudo cp $WD/deploy/rtc-service-SV.conf /etc/supervisor/conf.d/
sudo cp $WD/deploy/pass-go-service-SV.conf /etc/supervisor/conf.d/


mkdir -p /home/ubuntu/log
touch /home/ubuntu/log/rtc.err.log && touch /home/ubuntu/log/rtc.out.log
touch /home/ubuntu/log/pass-go.err.log && touch /home/ubuntu/log/pass-go.out.log

sudo apt -y update
sudo apt install -y nginx
sudo cp $WD/deploy/Pass-Go-NX /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

msg "${RED}Read parameters:${NOFORMAT}"
msg "- flag: ${flag}"
msg "- param: ${param}"
msg "- arguments: ${args[*]-}"