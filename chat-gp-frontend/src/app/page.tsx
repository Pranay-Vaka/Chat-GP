import { getAllCategories } from "@/api";

export default async function Home() {
  const categories = await getAllCategories();
  console.log(categories);

  return (
    <>
      <main className="w-full h-full grid place-items-center">
        <h2 className="text-black font-bold text-3xl mt-10">Which category are you interested in?</h2>
        <div className="flex justify-center items-center gap-5 mt-7">

          {categories.map((category) => (
            <div key={category.pk} className="card w-72 shadow-xl">
              <figure><img src={category.fields.image} alt={category.fields.name} /></figure>
              <div className="card-body">
                <h3 className="card-title text-black">{category.fields.name}</h3>
                <p className="text-slate-600">{category.fields.description}</p>
                <div className="card-actions justify-end">
                  <a href={category.fields.name} className="btn btn-primary text-white">Explore</a>
                </div>
              </div>
            </div>
          ))}

        </div>
      </main>
    </>
  );
}
