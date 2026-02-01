async function addNote() {
  const text = document.getElementById("note").value;

  await fetch("/api/notes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ note: text })
  });

  loadNotes();
}

async function loadNotes() {
  const res = await fetch("/api/notes");
  const data = await res.json();

  const list = document.getElementById("notes");
  list.innerHTML = "";
  data.forEach(n => {
    const li = document.createElement("li");
    li.innerText = n;
    list.appendChild(li);
  });
}

loadNotes();
