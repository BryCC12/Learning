#!/bin/bash
# Shell script para obtener una copia desde MySQL
# Desarrollado por Bry

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

set -e

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"

function assert_is_installed {
        local readonly name="$1"
        if [[ ! $(command -v ${name}) ]]; then
                log_error "The binary '$name' is required but it isn't in our system"
                exit 1
        fi
}

function log_error {
        local readonly message "$1"
        log "ERROR" "$message"
}

function  log {
        local readonly level="$1"
        local readonly message="$2"
        local readonly timestamp=$(date +"%Y-%m-%d %H:%M:%S") >&2 echo -e "${timestamp} [${level}] [$SCRIPT_NAME] ${message}"

}

function run {
        assert_is_installed "mysql"
        assert_is_installed "mysqldump"
        assert_is_installed "gzip"
}

function make_backup {
        local BAK="$(echo $HOME/mysql)"
        local MYSQL="$(which mysql)"
        local MYSQLDUMP="$(which mysqldump)"
        local GZIP="$(which gzip)"
        local NOW="$(date +"%d-%m-%Y")"
        local BUCKET="xxxxx"

        USER="nagios"
        PASS="Manager@2020"
        HOST="localhost"
        DATABASE="sexy"

        [ ! -d "$BAK" ] && mkdir -p "$BAK"

        FILE=$BAK/$DATABASE.$NOW-$(date +"%T").gz

        local SECONDS=0

        $MYSQLDUMP --single-transaction -u $USER -h $HOST -p$PASS $DATABASE | $GZIP -9 > $FILE

        duration=$SECONDS
        echo "$(($duration /60)) minutes"
}

run
make_backup