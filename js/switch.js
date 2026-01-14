let char = "a"
switch (char) {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u': document.writeln("vowel<br>");
        break;
    default: document.writeln("consonant<br>");
        break;
}
document.writeln("Outside the switch<br>")
