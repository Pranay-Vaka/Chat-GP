import React from 'react'

const Navbar = () => {
  return (
      <nav className="w-full bg-white flex justify-between items-center py-1 px-4">
        <header className="text-xl text-black font-semibold">ChatGP</header>
        <form>
          <input type="text" className="bg-slate-100 outline-none placeholder:font-light text-xs py-2 px-4 rounded-full" placeholder="Search ChatGP" />
        </form>
        <p className='text-black'>User</p>
      </nav>
  )
}

export default Navbar
