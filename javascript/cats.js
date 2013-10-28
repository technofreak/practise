/**
 * Created by Parthan on 10/21/13.
 *
 * Based on Chapter 4 of Eloquent Javascript
 *
 * Aunt Emily emails us about her cats every time she mails us. We want to record them and have a list of living cats at
 * any point in time. Also, she mentions the genealogy of her cats in her mails.
 *
 * Example:
 * born 21/04/2006 (mother Lady Gaga): Red Lion, Brave Jone
 * died 09/05/2006: General Hobbes
 *
 * Execution Plan:
 * 1. Go over the email archive, in chronological order
 * 2. Read the mail parah by parah, to start with 'born' or 'died'
 * 3. Add names of born cats to the list of living cats
 * 4. Remove the names of dead cats from the list of living cats
 */

var sample_archive = ["Hi, hope you're doing good.\nborn 10/21/2012: Chelsea\n",
                        "hi, how do you do?\nborn 03/13/2013 (mother Chelsea): Red Wood, Purple, Brownie",
                        "hola!\nborn 10/12/2013 (mother Purple): Woodwick, Chili, China\ndied 10/21/2013: Chelsea",
                        "am sad.\ndied 11/14/2013: Purple, China"];

var cat_data = {};

function retrieveMails() {
    return sample_archive;
}

function startsWith(text, word) {
    // returns true if text starts with word
    return (text.slice(0, word.length) == word);
}

function catNames(paragraph) {
    var colon = paragraph.indexOf(":");
    return paragraph.slice(colon+2).split(', ');
}

function parseDate(parah) {
    function getNumber(start, length) {
        return Number(parah.slice(start, start+length));
    }
    // offset month by -1 to start at 0 and end at 11
    return new Date(getNumber(11,4), getNumber(5,2)-1, getNumber(8,2));
}

function formatDate(date) {
    var month = date.getMonth() + 1;
    if (month < 10) { month = "0" + month; }
    return date.getDate() + "/" + month + "/" + date.getFullYear();
}

// function addToSet(set, values) {
//     for (var i = 0; i < values.length; i++) {
//         set[values[i]] = true;
//     }
// }

// function removeFromSet(set, values) {
//     for (var i = 0; i < values.length; i++) {
//         delete set[values[i]];
//     }
// }

function betweenStrings(paragraph, start, end) {
    var startAt = paragraph.indexOf(start);
    if (startAt > -1) {
        startAt += start.length;
        var endAt = paragraph.indexOf(end, startAt);
        return paragraph.slice(startAt, endAt);
    }
    return ""
}

function getMother(paragraph) {
    var start = '(mother ', end = ')';
    return betweenStrings(paragraph, start, end);

}

function catRecord(name, birthdate, mother) {
    return {name: name, birth: birthdate, mother: mother};
}

function addCats(set, names, birthdate, mother) {
    for (var i = 0; i < names.length; i++) {
        set[names[i]] = catRecord(names[i], birthdate, mother);
    }
}

function deadCats(set, names, deathdate) {
    for (var i = 0; i < names.length; i++) {
        set[names[i]].death = deathdate;
    }
}

function getLivingCats() {
    var mailArchive = retrieveMails();

    function handleParagraph(paragraph) {
        if (startsWith(paragraph, 'born')) {
            // var names = catNames(paragraphs[parah]);
            // for (var name = 0; name < names.length; name++) {
            //    living_cats[names[name]] = true;
            //}
            //addToSet(living_cats, catNames(paragraph));
            addCats(cat_data, catNames(paragraph), 
                parseDate(paragraph),
                getMother(paragraph));
        }
        else if (startsWith(paragraph, 'died')) {
            // var names = catNames(paragraphs[parah]);
            // for (var name = 0; name < names.length; name++) {
            //     delete living_cats[names[name]];
            // }
            //removeFromSet(living_cats, catNames(paragraph));
            deadCats(cat_data, catNames(paragraph),
                parseDate(paragraph));
        }
    }

    for (var mail = 0; mail < mailArchive.length; mail++) {
        var paragraphs = mailArchive[mail].split("\n");
        for (var parah = 0; parah < paragraphs.length; parah++) {
           handleParagraph(paragraphs[parah]);
        }
    }
    return cat_data;
}

function catInfo(data, name) {
    if (!(name in data)) {
        return "No cat named "+name+" is known.";
    }

    var cat = data[name];
    var message = name + ", born " + formatDate(cat.birth);
    if (cat.mother) {
        message += " from mother " + cat.mother;
    }
    if ("death" in cat) {
        message += ", died " + formatDate(cat.death);
    }

    return message + ".";
}

// TODO: this is not working as expected
function howManyLiving() {
    var howmany = 0;
    for (var cat in getLivingCats()) {
        if (! cat_data[cat].death) {
            howmany++;
        }
    }
    return howmany;
}

