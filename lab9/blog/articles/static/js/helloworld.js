// Группа студентов (как в Lab 1)
var groupmates = [
    { "name": "Василий", "group": "912-2", "age": 19, "marks": [4, 3, 5, 5, 4] },
    { "name": "Анна", "group": "912-1", "age": 18, "marks": [3, 2, 3, 4, 3] },
    { "name": "Георгий", "group": "912-2", "age": 19, "marks": [3, 5, 4, 3, 5] },
    { "name": "Валентина", "group": "912-1", "age": 18, "marks": [5, 5, 5, 4, 5] },
    { "name": "Дмитрий", "group": "912-2", "age": 20, "marks": [5, 4, 5, 5, 4] }
];

// Функция форматирования строки (аналог ljust)
var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length) str = str + ' ';
    return str;
};

// Вывод таблицы в консоль
var printStudents = function(students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
};

printStudents(groupmates);

// Задание: фильтрация по группе
var filterByGroup = function(students, group) {
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        if (students[i]['group'] === group) {
            filtered.push(students[i]);
        }
    }
    return filtered;
};

console.log("Студенты группы 912-2:");
printStudents(filterByGroup(groupmates, "912-2"));