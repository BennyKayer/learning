enum ResourceType {
  BOOK,
  AUTHOR,
  FILM,
  DIRECTOR,
  PERSON,
}

interface Resourcexd<T> {
  uid: number;
  resourceType: ResourceType;
  data: T;
}

const docXd: Resourcexd<object> = {
  uid: 1,
  resourceType: ResourceType.BOOK,
  data: { title: "name of the wind" },
};

const redAuth: Resourcexd<object> = {
  uid: 1,
  resourceType: ResourceType.AUTHOR,
  data: { name: "yoshi" },
};
