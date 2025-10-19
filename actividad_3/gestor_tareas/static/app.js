const apiUrl = "/api/tareas";
const lista = document.getElementById("lista-tareas");
const form = document.getElementById("form-tarea");
const titulo = document.getElementById("titulo");
const descripcion = document.getElementById("descripcion");
const prioridad = document.getElementById("prioridad");

document.addEventListener("DOMContentLoaded", cargarTareas);

async function cargarTareas() {
  try {
    const res = await fetch(apiUrl);
    const tareas = await res.json();

    lista.innerHTML = "";
    if (tareas.length === 0) {
      lista.innerHTML = "<p style='text-align:center;color:#475569;'>No hay tareas registradas.</p>";
      return;
    }

    tareas.forEach(t => {
      const card = document.createElement("div");
      card.classList.add("tarea-card");

      const tituloEl = document.createElement("h3");
      tituloEl.textContent = t.titulo;

      const descEl = document.createElement("p");
      descEl.textContent = t.descripcion || "Sin descripción.";

      const footer = document.createElement("div");
      footer.classList.add("tarea-footer");

      const prioridadEl = document.createElement("span");
      prioridadEl.classList.add("prioridad", t.prioridad);
      prioridadEl.textContent = t.prioridad;

      const acciones = document.createElement("div");
      acciones.classList.add("acciones");

      const btnCompletar = document.createElement("button");
      btnCompletar.textContent = t.completada ? "✅" : "⭕";
      btnCompletar.title = "Marcar como completada";
      btnCompletar.onclick = () => marcarCompletada(t);

      const btnBorrar = document.createElement("button");
      btnBorrar.textContent = "🗑️";
      btnBorrar.title = "Eliminar tarea";
      btnBorrar.onclick = () => eliminarTarea(t.id);

      acciones.append(btnCompletar, btnBorrar);
      footer.append(prioridadEl, acciones);

      card.append(tituloEl, descEl, footer);
      lista.append(card);
    });
  } catch (error) {
    console.error("Error al cargar tareas:", error);
  }
}

form.onsubmit = async (e) => {
  e.preventDefault();
  const nueva = {
    titulo: titulo.value,
    descripcion: descripcion.value,
    prioridad: prioridad.value,
    completada: false,
  };
  await fetch(apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(nueva),
  });
  form.reset();
  await cargarTareas(); // recargar lista
};

async function eliminarTarea(id) {
  await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
  await cargarTareas();
}

async function marcarCompletada(t) {
  t.completada = !t.completada;
  await fetch(`${apiUrl}/${t.id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(t),
  });
  await cargarTareas();
}
