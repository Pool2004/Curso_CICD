async function addContact(event) {
    event.preventDefault(); // Evita recargar la página

    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (!name || !phone) {
        alert("Por favor completa todos los campos antes de guardar.");
        return;
    }

    const formData = new FormData();
    formData.append("name", name);
    formData.append("phone", phone);

    try {
        const response = await fetch("/add", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            alert("✅ Contacto agregado exitosamente");
            window.location.href = "/";
        } else {
            alert("❌ No se pudo agregar el contacto");
        }
    } catch (error) {
        console.error("Error al agregar:", error);
        alert("⚠️ Ocurrió un error al conectar con el servidor.");
    }
}

async function updateContact(event, contactId) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (!name || !phone) {
        alert("Por favor completa todos los campos antes de actualizar.");
        return;
    }

    const formData = new FormData();
    formData.append("name", name);
    formData.append("phone", phone);

    try {
        const response = await fetch(`/update/${contactId}`, {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            alert("✏️ Contacto actualizado correctamente");
            window.location.href = "/";
        } else {
            alert("❌ No se pudo actualizar el contacto");
        }
    } catch (error) {
        console.error("Error al actualizar:", error);
        alert("⚠️ Error de conexión con el servidor.");
    }
}

async function deleteContact(contactId) {
    if (confirm("¿Estás seguro de eliminar este contacto?")) {
        try {
            const response = await fetch(`/delete/${contactId}`, { method: "GET" });

            if (response.ok) {
                alert("🗑️ Contacto eliminado correctamente");
                window.location.reload();
            } else {
                alert("❌ No se pudo eliminar el contacto");
            }
        } catch (error) {
            console.error("Error al eliminar:", error);
            alert("⚠️ Error al conectar con el servidor.");
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contactForm");
    const editForm = document.getElementById("editForm");
    if (form) {
        form.addEventListener("submit", addContact);
    }
    if (editForm) {
        const contactId = editForm.getAttribute("data-id");
        editForm.addEventListener("submit", (event) => updateContact(event, contactId));
    }
    const deleteButtons = document.querySelectorAll(".delete-btn");
    deleteButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const id = btn.getAttribute("data-id");
            deleteContact(id);
        });
    });
});
