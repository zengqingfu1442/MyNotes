---https://www.youtube.com/watch?v=ZEBb1JV8PSc
--- 无密版代码：
@echo off
md D:\RECYCLED\UDrives.{25336920-03F9-11CF-8FD0-00AA00686F13}>NUL
if exist M:\NUL goto delete
subst M: D:\RECYCLED\UDrives.{25336920-03F9-11CF-8FD0-00AA00686F13}
start M:\
goto end
:delete
subst /D M:
:end

---加密版代码：
@echo off
set ci=3
echo.
echo 注意： 三次输入错误将退出.
echo.
:1
set /p mima=请输入密码：
if \"%mima%\"==\"lingdu\" goto o
set /a ci-=1
if \"%ci%\"==\"0\" cls&echo.&echo =没密码无法进入=&echo.&pause&echo.&exit
cls&echo.&echo 你还有 %ci% 次机会&echo.&goto 1
:o
cls&echo.
echo= 密码正权确，放行 =
md D:\RECYCLED\UDrives.{25336920-03F9-11CF-8FD0-00AA00686F13}>NUL
if exist M:\NUL goto delete
subst M: D:\RECYCLED\UDrives.{25336920-03F9-11CF-8FD0-00AA00686F13}
start M:\
goto end
:delete
subst /D M:
:end
echo.&pause&exit.
