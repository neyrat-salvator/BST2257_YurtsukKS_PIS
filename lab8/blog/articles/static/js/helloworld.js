var groupmates = [
    {
        "name": "Василий",
        "group" : "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group" : "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Георгий",
        "group" : "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 4]
    },
    {
        "name": "Валентина",
        "group" : "912-1",
        "age": 18,
        "marks": [5, 5, 5, 5, 4]
    },
    {
        "name": "Дмитрий",
        "group" : "912-2",
        "age": 20,
        "marks": [4, 4, 5, 5, 4]
    },
];

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length) {
        str = str + " ";
    }
    
    return str;
};

var printStudents = function(students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );

    for (var i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i]["name"], 15),
            rpad(students[i]["group"], 8),
            rpad(students[i]["age"], 8),
            rpad(students[i]["marks"], 20)
        );
    }
    console.log("\n");
};

var filterByGroup = function(students, groupName) {
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        if (students[i]["group"] == groupName) {
            filtered.push(students[i]);
        };
    };

    return filtered;
};

var filterByAverageMark = function(students, minAverage) {
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        var marks = students[i]["marks"];
        var sum = 0;
        for (var j = 0; j < marks.length; j++) {
            sum += marks[j];
        }

        var average = sum / marks.length;
        if (average >= minAverage) {
            filtered.push(students[i]);
        }
    }

    return filtered;
};

console.log("=== Все студенты ===");
printStudents(groupmates);

console.log("=== Студенты группы 912-2 ===");
var group912_2 = filterByGroup(groupmates, "912-2");
printStudents(group912_2);

console.log("=== Студенты группы со средней оценкой >= 4 ===");
var group912_2 = filterByAverageMark(groupmates, 4);
printStudents(group912_2);