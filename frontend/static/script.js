document.addEventListener('DOMContentLoaded', () => {
    
    // --- Navigation Logic ---
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.content-section');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove active class from all nav items and sections
            navItems.forEach(nav => nav.classList.remove('active'));
            sections.forEach(sec => sec.classList.remove('active'));

            // Add active class to clicked nav item
            item.classList.add('active');

            // Show corresponding section
            const targetId = item.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');
            
            // Fetch relevant data if needed when switching sections
            if (targetId === 'dataset') fetchGallery('results/visualizations', 'dataset-gallery');
            if (targetId === 'baseline') fetchGallery('results/visualizations/baseline/rgb', 'baseline-gallery');
            if (targetId === 'metrics') fetchGallery('results/visualizations/metrics', 'metrics-gallery');
            if (targetId === 'architecture') fetchGallery('docs', 'architecture-gallery');
            if (targetId === 'efficiency') fetchGallery('results/visualizations/failures', 'efficiency-gallery');
        });
    });

    // --- Dashboard Stats Fetching ---
    function fetchStats() {
        fetch('/api/stats')
            .then(res => res.json())
            .then(data => {
                document.getElementById('stat-dataset').textContent = data.dataset || 'Ready';
                document.getElementById('stat-ap').textContent = data.baseline_ap || 'N/A';
                document.getElementById('stat-fps').textContent = data.baseline_fps || 'N/A';
                
                if(document.getElementById('stat-cmaf-ap')) {
                    document.getElementById('stat-cmaf-ap').textContent = data.cmaf_ap || 'N/A';
                }
                if(document.getElementById('stat-cmaf-fps')) {
                    document.getElementById('stat-cmaf-fps').textContent = data.cmaf_fps || 'N/A';
                }
            })
            .catch(err => console.error("Error fetching stats:", err));
    }
    
    // Initial fetch
    fetchStats();

    // --- Image Gallery Fetching ---
    function fetchGallery(folderName, containerId) {
        const container = document.getElementById(containerId);
        
        fetch(`/api/files/${folderName}`)
            .then(res => res.json())
            .then(files => {
                if (files && files.length > 0) {
                    container.innerHTML = ''; // clear empty state
                    files.forEach(file => {
                        const img = document.createElement('img');
                        img.src = `/media/${folderName}/${file}`;
                        img.alt = file;
                        img.title = file;
                        
                        // Add a wrapper for aesthetic
                        const wrapper = document.createElement('div');
                        wrapper.classList.add('img-wrapper');
                        wrapper.appendChild(img);
                        
                        container.appendChild(wrapper);
                    });
                }
            })
            .catch(err => console.error(`Error fetching images for ${folderName}:`, err));
    }
});
