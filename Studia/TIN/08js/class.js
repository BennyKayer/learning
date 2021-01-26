const switchClassName = (obj, className) => {
    let arrayed = obj.className.split(" ");
    let i = arrayed.indexOf(className);
    let index = i === -1 ? arrayed.length : i;
    let howMany = i === -1 ? 0 : 1;
    let item = i === -1 ? className : null;
    arrayed.splice(index, howMany, item);
    arrayed = arrayed.filter(el => el !== null);
    obj.className = arrayed.join(" ");
};
