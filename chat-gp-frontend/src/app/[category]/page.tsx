import React from 'react'
import Navbar from '../Navbar'
import { categories } from '@/constants'

type PageParams = {
  params: {
    category: string
  }
}

const CategoryPage = ({ params: { category } }: PageParams) => {
  if (!categories.map(x => x.path).includes(category)) {
    return (
      <>
        <div className="absolute w-screen h-screen bg-slate-200 -z-10"></div>
        <Navbar />
        <main className="w-full h-full grid place-items-center">
          <h2 className="text-black font-bold text-3xl mt-10">Category {category} not found!</h2>
          <a className='pt-3' href='/'>Return to main page</a>
        </main>
      </>
    )
  }
  return (
    <>
      <div className="absolute w-screen h-screen bg-slate-200 -z-10"></div>
      <Navbar />
      <main className="w-full h-full grid place-items-center">
        <h2 className="text-black font-bold text-3xl mt-10">{category}</h2>
        <div className="flex justify-center items-center gap-5 mt-5">

        </div>
      </main>
    </>
  )
}

export default CategoryPage
