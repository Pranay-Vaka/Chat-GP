import React from 'react'
import { categories, topics } from '@/constants'

type PageParams = {
  params: {
    category: string
  }
}

const CategoryPage = ({ params: { category } }: PageParams) => {
  const categoryData = categories.find(x => x.path === category)

  if (!categoryData) {
    return (
      <>
        <main className="w-full h-full grid place-items-center">
          <h2 className="text-black font-bold text-3xl mt-10">Category {category} not found</h2>
          <a className='pt-3' href='/'>Return to main page</a>
        </main>
      </>
    )
  }

  const categoryTopics = topics.filter(x => x.parent === categoryData.name);

  return (
    <>
      <main className="w-full h-full grid place-items-center">
        <h2 className="text-black font-bold text-3xl mt-10">{categoryData.name}</h2>
        <p>Explore these topics</p>

        <div className="flex justify-center items-center gap-5 mt-7">

          {categoryTopics.map((categoryTopic) => (
            <div className="card bg-slate-100 w-72 shadow-xl">
              <figure><img src={categoryTopic.image} alt={categoryTopic.name} /></figure>
              <div className="card-body">
                <h3 className="card-title text-black">{categoryTopic.name}</h3>
                <p className="text-slate-600">Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.</p>
                <div className="card-actions justify-end">
                  <a href={categoryTopic.path} className="btn btn-primary text-white">Explore</a>
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
