# 1cv8-base-migration
 Migrate 1C ibases,v8i

After migration bases to new server if you need to change path of bases for all users in server, then with use this script you can quickly switch your customers.


После переноса информационной базы на новый сервер возникла проблема изменения настроек информационных баз 1С. Для миграции был написан данный скрипт, он позволяет сканировать рекурсивно папки Users, искать там файлы *.v8i и прописывать новое  расположение базы вместо старого. 
