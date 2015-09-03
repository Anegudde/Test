TITLE= Node2
rem set Directory to D:\Work\Drivers\
d:
cd D:\Work\Drivers\ 
java -jar selenium-server-standalone-2.42.0.jar -role node  -hub http://localhost:4444/grid/register  -nodeConfig NodeConfig.json -port 5556
