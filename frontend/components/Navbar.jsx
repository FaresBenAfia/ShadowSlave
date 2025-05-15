// components/Navbar.jsx
import Link from "next/link";
import Image from "next/image";
import "../styles/navbar.css";

export default function Navbar() {
  return (
    <div className="navbar">
      <div className="logo-links">
        <Image
          src="/assets/Mask.png"
          alt="Shadow Slave Logo"
          width={80} // Adjust based on your logo size
          height={80}
          priority // Optional: for above-the-fold images
        />
        <p className="logo-text">Shadow Slave</p>
        <ul className="links">
          <li>
            <Link href="/">Home</Link>
          </li>
          <li>
            <Link href="/plot">Plot</Link>
          </li>
          <li>
            <Link href="/characters">Characters</Link>
          </li>
          <li>
            <Link href="/gallery">Gallery</Link>
          </li>
          <li>
            <Link href="/author">Author</Link>
          </li>
        </ul>
      </div>
      <div className="auth">
        <ul>
          <li>
            <Link href="/login">Login</Link>
          </li>
          <li>
            <Link href="/register">Register</Link>
          </li>
        </ul>
      </div>
    </div>
  );
}