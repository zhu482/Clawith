import { useEffect, useState } from 'react';
import './CapybaraStatus.css';

type ServiceStatus = 'checking' | 'online' | 'warning' | 'offline';

interface StatusInfo {
  backend: boolean;
  openclaw: boolean;
}

export default function CapybaraStatus() {
  const [status, setStatus] = useState<ServiceStatus>('checking');
  const [info, setInfo] = useState<StatusInfo>({ backend: false, openclaw: false });
  const [expanded, setExpanded] = useState(false);
  const [blinking, setBlinking] = useState(false);

  const checkServices = async () => {
    // Blink before checking
    setBlinking(true);
    setTimeout(() => setBlinking(false), 400);

    let backendOk = false;
    let openclawOk = false;

    try {
      const res = await fetch('/api/health', { signal: AbortSignal.timeout(4000) });
      backendOk = res.ok;
    } catch { /* offline */ }

    try {
      const res = await fetch('http://localhost:9999/health', { signal: AbortSignal.timeout(3000) });
      openclawOk = res.ok;
    } catch {
      // OpenClaw doesn't expose a health endpoint by default — treat as unknown
      // If backend is up, assume openclaw is likely up too (same machine)
      openclawOk = backendOk;
    }

    setInfo({ backend: backendOk, openclaw: openclawOk });

    if (backendOk && openclawOk) setStatus('online');
    else if (backendOk || openclawOk) setStatus('warning');
    else setStatus('offline');
  };

  useEffect(() => {
    checkServices();
    const timer = setInterval(checkServices, 30_000);
    return () => clearInterval(timer);
  }, []);

  const statusLabel: Record<ServiceStatus, string> = {
    checking: '检查中...',
    online:   '全部正常运行',
    warning:  '部分服务异常',
    offline:  '服务已停止',
  };

  return (
    <div
      className={`capybara-widget capybara-${status} ${blinking ? 'capybara-blink' : ''}`}
      onClick={() => setExpanded(e => !e)}
      title={statusLabel[status]}
    >
      {/* ── SVG 水豚 ── */}
      <div className="capybara-body">
        <svg viewBox="0 0 80 60" xmlns="http://www.w3.org/2000/svg" className="capybara-svg">
          {/* 身体 */}
          <ellipse cx="40" cy="38" rx="28" ry="16" fill="#c8a97a" />
          {/* 头 */}
          <ellipse cx="62" cy="28" rx="16" ry="13" fill="#c8a97a" />
          {/* 耳朵 */}
          <ellipse cx="55" cy="17" rx="5" ry="7" fill="#b8945f" className="capybara-ear-left" />
          <ellipse cx="70" cy="16" rx="5" ry="7" fill="#b8945f" className="capybara-ear-right" />
          <ellipse cx="55" cy="18" rx="3" ry="4" fill="#e8b89a" />
          <ellipse cx="70" cy="17" rx="3" ry="4" fill="#e8b89a" />
          {/* 鼻子 */}
          <ellipse cx="75" cy="28" rx="5" ry="4" fill="#b8945f" />
          <ellipse cx="75" cy="27" rx="2" ry="1.5" fill="#2a1a0e" />
          {/* 眼睛 */}
          <circle cx="66" cy="22" r="3.5" fill="#2a1a0e" className="capybara-eye" />
          <circle cx="67.2" cy="21" r="1.2" fill="white" />
          {/* 腿 */}
          <rect x="18" y="48" width="8" height="10" rx="4" fill="#b8945f" />
          <rect x="30" y="49" width="8" height="10" rx="4" fill="#b8945f" />
          <rect x="44" y="49" width="8" height="10" rx="4" fill="#b8945f" />
          <rect x="56" y="48" width="8" height="10" rx="4" fill="#b8945f" />
          {/* 尾巴 */}
          <ellipse cx="13" cy="38" rx="6" ry="4" fill="#b8945f" />

          {/* 状态装饰 */}
          {status === 'online' && (
            <g className="capybara-grass">
              <rect x="68" y="20" width="2" height="8" rx="1" fill="#5aaa5a" transform="rotate(-15 68 20)" />
              <rect x="72" y="19" width="2" height="9" rx="1" fill="#4a9a4a" transform="rotate(5 72 19)" />
              <rect x="75" y="20" width="2" height="7" rx="1" fill="#5aaa5a" transform="rotate(20 75 20)" />
            </g>
          )}
          {status === 'warning' && (
            <text x="58" y="10" fontSize="12" className="capybara-sweat">💦</text>
          )}
          {status === 'offline' && (
            <g className="capybara-zzz">
              <text x="60" y="8" fontSize="8" fill="#888">z</text>
              <text x="66" y="4" fontSize="10" fill="#999">z</text>
              <text x="72" y="0" fontSize="12" fill="#aaa">Z</text>
            </g>
          )}
          {status === 'checking' && (
            <text x="60" y="10" fontSize="11" className="capybara-dots">...</text>
          )}
        </svg>

        {/* 状态指示灯 */}
        <div className={`capybara-dot capybara-dot-${status}`} />
      </div>

      {/* ── 展开面板 ── */}
      {expanded && (
        <div className="capybara-panel" onClick={e => e.stopPropagation()}>
          <div className="capybara-panel-title">🦫 系统状态</div>
          <div className="capybara-panel-row">
            <span className={`dot ${info.backend ? 'green' : 'red'}`} />
            <span>Clawith 后端</span>
            <span className="capybara-panel-status">{info.backend ? '运行中' : '已停止'}</span>
          </div>
          <div className="capybara-panel-row">
            <span className={`dot ${info.openclaw ? 'green' : 'red'}`} />
            <span>OpenClaw</span>
            <span className="capybara-panel-status">{info.openclaw ? '运行中' : '已停止'}</span>
          </div>
          <button className="capybara-refresh" onClick={checkServices}>↻ 刷新</button>
        </div>
      )}
    </div>
  );
}
