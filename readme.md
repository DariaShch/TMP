# Нулевая лабораторная работа по ТМП

## Выполнила: Щепетова Д.В. БИСО-03-20

```
@startuml
left to right direction
skinparam packageStyle rect
actor Пользователь
actor Система
rectangle Сервис {
  Пользователь -- (Подать запрос на регистрацию)
  Пользователь-- (Подключиться к системе)
  Пользователь- (Отправлять сообщения)
  Пользователь- (Получать сообщения)
  Пользователь-- (Отключиться от системы)
  Пользователь-- (Подать запрос на аннуляцию)
  Система -- (Зарегестрировать пользователя)
  Система -- (Аннулировать пользователя)
  (Подать запрос на регистрацию) .> (Зарегестрировать пользователя) : регистрация
  (Подать запрос на аннуляцию) .> (Аннулировать пользователя) : аннуляция
}
@enduml
```
# Первая лабораторная работа по ТМП
```
@startuml
left to right direction
skinparam packageStyle rect
actor Пользователь
actor Администратор
rectangle Сервис {
  Пользователь -- (Подать запрос на регистрацию)
  Пользователь-- (Подключиться к системе)
  Пользователь- (Отправлять сообщения)
  Пользователь- (Получать сообщения)
  Пользователь-- (Отключиться от системы)
  Пользователь-- (Подать запрос на аннуляцию)
  Администратор -- (Зарегестрировать пользователя)
  Администратор -- (Аннулировать пользователя)
  (Подать запрос на регистрацию) .> (Зарегестрировать пользователя) : регистрация
  (Подать запрос на аннуляцию) .> (Аннулировать пользователя) : аннуляция
}
@enduml

@startuml 
class Пользователь{
  +Фамилия
  +Имя
  +Отчество
  +Ник
  +Почта
  +Пароль
  Отправка сообщения()
  Получение сообщения()
}
class Сообщение{
  +Отправитель
  +Получатель
  +Время отправления
  +Содержание
}
class Администратор{
  +Фамилия
  +Имя
  +Отчество
  +Паспортные данные
}
class Сервис{
  +Активные пользователи
}
Пользователь -> Сообщение: отправка
Пользователь -> Сообщение: получение
Пользователь -> Сервис: подключение
Пользователь -> Сервис: отключение
Администратор -> Пользователь: регистрация
Администратор -> Пользователь: аннуляция
@enduml
```
# Вторая лабораторная работа по ТМП
```
@startuml
participant Администратор
participant Пользователь
participant Сервис
participant Сообщение
activate Сервис
activate Пользователь
Пользователь -> Администратор: запрос на регистрацию
activate Администратор
Администратор -> Пользователь: регистрация 
deactivate Администратор
Пользователь -> Сервис: подключение
Пользователь -> Сообщение: Отправка сообщения
activate Сообщение
Сообщение -> Пользователь: получение сообщения
deactivate Сообщение 
Пользователь -> Сообщение: Отправка сообщения
activate Сообщение
Сообщение -> Пользователь: получение сообщения
deactivate Сообщение 
Пользователь -> Сообщение: Отправка сообщения
activate Сообщение
Сообщение -> Пользователь: получение сообщения
deactivate Сообщение 
Пользователь -> Сервис: отключение
deactivate Пользователь
Пользователь -> Сервис: подключение
Пользователь -> Сообщение: Отправка сообщения
activate Сообщение
Сообщение -> Пользователь: получение сообщения
deactivate Сообщение 
Пользователь -> Сообщение: Отправка сообщения
activate Сообщение
Сообщение -> Пользователь: получение сообщения
deactivate Сообщение
activate  Пользователь
Пользователь -> Администратор: запрос на аннуляцию
activate Администратор
Администратор -> Пользователь: аннуляция
deactivate Администратор
deactivate Пользователь
deactivate Сервис
@enduml

@startuml
node Пользователь
node Администратор
database Сервис
database Сообщение 
Пользователь .. Администратор: запрос на регистрацию/аннуляцию
Администратор - Пользователь: регистрация/аннулция
Пользователь - Сервис: подключение
Пользователь .. Сервис: отключение
Пользователь - Сообщение: отправка
Пользователь .. Сообщение: получение
@enduml
```
