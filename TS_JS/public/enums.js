"use strict";
var ResourceType;
(function (ResourceType) {
    ResourceType[ResourceType["BOOK"] = 0] = "BOOK";
    ResourceType[ResourceType["AUTHOR"] = 1] = "AUTHOR";
    ResourceType[ResourceType["FILM"] = 2] = "FILM";
    ResourceType[ResourceType["DIRECTOR"] = 3] = "DIRECTOR";
    ResourceType[ResourceType["PERSON"] = 4] = "PERSON";
})(ResourceType || (ResourceType = {}));
const docXd = {
    uid: 1,
    resourceType: ResourceType.BOOK,
    data: { title: "name of the wind" },
};
const redAuth = {
    uid: 1,
    resourceType: ResourceType.AUTHOR,
    data: { name: "yoshi" },
};
