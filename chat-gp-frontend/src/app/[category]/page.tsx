import React from 'react'
import { getAllForums } from "@/api";

type PageParams = {
  params: {
    category: string
  }
}
const CategoryPage = async ({ params: { category } }: PageParams) => {
  const forumsResponse = await getAllForums(category);

  if (!forumsResponse.ok) {
    return (
      <>
        <main className="w-full h-full grid place-items-center">
          <h2 className="text-black font-bold text-3xl mt-10">Category {category} not found</h2>
          <a className='pt-3' href='/'>Return to main page</a>
        </main>
      </>
    )
  }

  const forums = forumsResponse.forums;

  return (
    <>
      <main className="w-full h-full grid place-items-center">
        <h2 className="text-black font-bold text-3xl mt-10">{category}</h2>
        <p>Explore these topics</p>

        <div className="flex justify-center items-center gap-5 mt-7">

          {forums.map((forum) => (
            <div className="card w-72 min-h-[40rem] shadow-xl">
              <figure><img src={forum.fields.image} alt={forum.fields.name} /></figure>
              <div className="card-body">
                <h3 className="card-title text-black">{forum.fields.name}</h3>
                <p className="text-slate-600">{forum.fields.description}</p>
                <div className="card-actions justify-end">
                  <a href={`${category}/${forum.fields.name}`} className="btn btn-primary text-white">Explore</a>
                </div>
              </div>
            </div>
          ))}
        </div>

      </main>
    </>
  )
}

export default CategoryPage

