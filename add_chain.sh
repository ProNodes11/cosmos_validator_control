add_chain_config() {
    local file=$1
    local chain_name=$2
    local chain_id=$3
    local valoper_address=$4
    local rpc_url=$5
    local alert_if_no_servers=$6
    local telegram_api_key=$7
    local telegram_channel=$8

    # Проверяем, существует ли уже блок для данной сети
    if grep -q "$chain_name:" "$file"; then
        echo "Chain '$chain_name' already exists in $file. Exiting."
        exit 1
    fi

    # Добавляем новый блок конфигурации в файл
    cat >> "$file" <<EOL

  "$chain_name":
    chain_id: $chain_id
    valoper_address: $valoper_address
    public_fallback: yes
    alerts:
      stalled_enabled: yes
      stalled_minutes: 10
      consecutive_enabled: yes
      consecutive_missed: 5
      consecutive_priority: critical
      percentage_enabled: no
      percentage_missed: 10
      percentage_priority: warning
      alert_if_inactive: yes
      alert_if_no_servers: yes
      telegram:
        enabled: yes
        api_key: ""
        channel: ""
    nodes:
      - url: $rpc_url
        alert_if_down: yes
      - url: $rpc_2_url
        alert_if_down: no
EOL
}
# Запрос параметров сети
echo "Введите параметры сети для добавления в config.yml"

read -p "Введите название сети(важно ввести маленькми буквами и правильно, например, persistence): " chain_name
read -p "Введите chain_id: " chain_id
read -p "Введите valoper_address: " valoper_address
read -p "Введите URL RPC сервера(формат tcp://ip:port): " rpc_url
read -p "Введите URL публичное  RPC(можно поискать на полкачу): " rpc_2_url
# Определение файла конфигурации
config_file="config.yml"
VALIDATOR_API="https://validators.cosmos.directory/chains/"
CONCRETE_VALIDATOR_API="${VALIDATOR_API}${chain_name}/${valoper_address}"
# Добавление новой сети в config.yml
echo "Добавление новой сети в $config_file..."
add_chain_config "$config_file" "$chain_name" "$chain_id" "$valoper_address" "$rpc_url" "$alert_if_no_servers" "$telegram_api_key" "$telegram_channel"
FILE_PATH="validator_list.txt"
CONTENT=$(cat "$FILE_PATH")
echo "$CONCRETE_VALIDATOR_API"
echo $VALIDATOR_API
if [[ "$CONTENT" == "[]" ]]; then
    # Если файл содержит пустой список []
    echo "[\"$CONCRETE_VALIDATOR_API\"]" > "$FILE_PATH"
else
    content=$CONTENT
    content=${content%?}
    echo "${content},\"$CONCRETE_VALIDATOR_API\"]" > "$FILE_PATH"
fi

echo "Добавление завершено. Проверьте $config_file для подтверждения изменений."
