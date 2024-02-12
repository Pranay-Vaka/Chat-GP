import { categories } from "@/constants";
import Navbar from "./Navbar";

export default function Home() {
  return (
    <>
      <div className="absolute w-screen h-screen bg-slate-200 -z-10"></div>
      <Navbar />
      <main className="w-full h-full grid place-items-center">
        <h2 className="text-black font-bold text-3xl mt-10">Which category are you interested in?</h2>
        <div className="flex justify-center items-center gap-5 mt-5">

          {categories.map((category) => (
            <div className="card w-72 shadow-xl">
              <figure><img src={category.image} alt={category.name} /></figure>
              <div className="card-body">
                <h2 className="card-title text-black">{category.name}</h2>
                <p className="text-slate-600">Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.</p>
                <div className="card-actions justify-end">
                  <a href={category.path} className="btn btn-primary text-white">Explore</a>
                </div>
              </div>
            </div>
          ))}

        </div>
      </main>
    </>
  );
}
