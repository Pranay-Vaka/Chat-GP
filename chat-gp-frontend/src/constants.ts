export type Category = {
  name: string,
  path: string,
  image: string
}

export const categories = [
  {
    name: "Cancer",
    path: "cancer",
    image: "https://images.pexels.com/photos/579474/pexels-photo-579474.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
  {
    name: "Diabetes",
    path: "diabetes",
    image: "https://images.pexels.com/photos/5469026/pexels-photo-5469026.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
  {
    name: "Heart disease",
    path: "heart-disease",
    image: "https://images.pexels.com/photos/4386466/pexels-photo-4386466.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
] as const

export type Topic<T extends typeof categories[number]> = {
  parent: T["name"],
  path: `${T["path"]}/${string}`,
  name: string,
  image: string
}

export const topics: Topic<typeof categories[number]>[] = [
  {
    parent: "Cancer",
    path: "cancer/breast-cancer",
    name: "Breast cancer",
    image: "https://images.pexels.com/photos/3900427/pexels-photo-3900427.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
  {
    parent: "Diabetes",
    path: "diabetes/type-1-diabetes",
    name: "Type 1 diabetes",
    image: "https://images.pexels.com/photos/6941884/pexels-photo-6941884.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
  {
    parent: "Heart disease",
    path: "heart-disease/heart-disease",
    name: "Heart disease",
    image: "https://images.pexels.com/photos/263402/pexels-photo-263402.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  },
]
